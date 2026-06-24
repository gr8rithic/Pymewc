import time

__version__ = "0.2.0"
__author__ = "Rithic C H"
__email__ = "gr8rithic@gmail.com"
__license__ = "MIT"

__all__ = [
    "hello",
    "about",
    "list_ports",
    "serial",
    "serial_discrete",
    "scope",
    "blink",
    "digital_write",
]


def hello():
    print(f"Hello world, pymewc {__version__} is installed correctly.")


def about():
    print(f"pymewc {__version__} - Python Microcontroller Interface")
    print(f"Author:    {__author__} <{__email__}>")
    print("GitHub:    https://github.com/gr8rithic/")
    print("LinkedIn:  https://www.linkedin.com/in/rithic-hariharan-8902b4199/")
    print("Portfolio: https://gr8rithic.github.io/")
    print(f"To report an issue, email {__email__}.")


def list_ports():
    from serial.tools import list_ports as _list_ports

    return [port.device for port in _list_ports.comports()]


def _prompt_port(com_port):
    if com_port is not None:
        return com_port
    try:
        available = list_ports()
    except Exception:
        available = []
    if available:
        print("Available serial ports:", ", ".join(available))
    return input("Enter the COM port (e.g. COM4 or /dev/ttyACM0): ").strip()


def _prompt_int(value, prompt):
    if value is not None:
        return int(value)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def _prompt_float(value, prompt):
    if value is not None:
        return float(value)
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number.")


def _connect(com_port):
    import pyfirmata2

    try:
        return pyfirmata2.Arduino(com_port)
    except OSError as exc:
        print(f"Could not connect to {com_port!r}: {exc}")
        print("Check that the device is connected and the port name is correct.")
        return None


def _read_serial(com_port, baud_rate, count):
    import serial

    com_port = _prompt_port(com_port)
    baud_rate = _prompt_int(baud_rate, "Enter the baud rate (as set in the .ino sketch): ")

    try:
        connection = serial.Serial(com_port, baud_rate)
    except (serial.SerialException, ValueError, OSError) as exc:
        print(f"Could not open {com_port!r} at {baud_rate} baud: {exc}")
        print("Check that the device is connected and the port name is correct.")
        return

    read = 0
    try:
        while count is None or read < count:
            try:
                line = connection.readline().strip().decode("utf-8")
            except UnicodeDecodeError:
                continue
            print(line)
            read += 1
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        connection.close()


def serial(com_port=None, baud_rate=None):
    _read_serial(com_port, baud_rate, count=None)


def serial_discrete(count=None, com_port=None, baud_rate=None):
    count = _prompt_int(count, "Enter the number of readings to stream: ")
    _read_serial(com_port, baud_rate, count=count)


def scope(com_port=None, analog_pin=0, sampling_rate=100, window=500):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

    com_port = _prompt_port(com_port)

    class RealtimePlotWindow:
        def __init__(self):
            self.fig, self.ax = plt.subplots(figsize=(9, 4.5))
            manager = self.fig.canvas.manager
            if manager is not None:
                manager.set_window_title(f"pymewc scope - A{analog_pin}")

            self.fig.patch.set_facecolor("#0b0f17")
            self.ax.set_facecolor("#0b0f17")

            self.timebase = np.linspace(-window / sampling_rate, 0, window)
            self.plotbuffer = np.zeros(window)
            (self.line,) = self.ax.plot(
                self.timebase,
                self.plotbuffer,
                color="#39ff14",
                linewidth=1.5,
                solid_capstyle="round",
            )
            self.glow = [
                self.ax.plot(
                    self.timebase,
                    self.plotbuffer,
                    color="#39ff14",
                    linewidth=1.5 + 2 * level,
                    alpha=0.06,
                    solid_capstyle="round",
                )[0]
                for level in range(1, 4)
            ]

            self.ax.set_ylim(0, 1.5)
            self.ax.set_xlim(self.timebase[0], self.timebase[-1])
            self.ax.set_title(f"Analog pin A{analog_pin} at {sampling_rate} Hz", color="#cfd8dc")
            self.ax.set_xlabel("Time (s)", color="#cfd8dc")
            self.ax.set_ylabel("Normalised value", color="#cfd8dc")
            self.ax.tick_params(colors="#90a4ae")
            for spine in self.ax.spines.values():
                spine.set_color("#37474f")
            self.ax.grid(True, color="#1b2735", linestyle="--", linewidth=0.6)

            self.readout = self.ax.text(
                0.02,
                0.95,
                "",
                transform=self.ax.transAxes,
                color="#39ff14",
                family="monospace",
                fontsize=11,
                va="top",
            )

            self.fig.tight_layout()
            self.ringbuffer = []
            self.ani = animation.FuncAnimation(
                self.fig, self.update, interval=100, cache_frame_data=False
            )

        def update(self, _frame):
            self.plotbuffer = np.append(self.plotbuffer, self.ringbuffer)
            self.plotbuffer = self.plotbuffer[-window:]
            self.ringbuffer = []
            self.line.set_ydata(self.plotbuffer)
            for trace in self.glow:
                trace.set_ydata(self.plotbuffer)
            self.readout.set_text(f"A{analog_pin} = {self.plotbuffer[-1]:.3f}")
            return (self.line, self.readout, *self.glow)

        def add_data(self, value):
            self.ringbuffer.append(value)

    board = _connect(com_port)
    if board is None:
        return

    plot_window = RealtimePlotWindow()
    try:
        board.samplingOn(1000 / sampling_rate)
        board.analog[analog_pin].register_callback(plot_window.add_data)
        board.analog[analog_pin].enable_reporting()
        plt.show()
    finally:
        board.exit()
    print("The scope has been closed.")


def blink(pin=None, delay_sec=None, com_port=None, count=None):
    pin = _prompt_int(pin, "Enter the digital pin to blink: ")
    delay_sec = _prompt_float(delay_sec, "Enter the delay between blinks in seconds: ")
    com_port = _prompt_port(com_port)

    board = _connect(com_port)
    if board is None:
        return

    blinks = 0
    try:
        while count is None or blinks < count:
            board.digital[pin].write(1)
            time.sleep(delay_sec)
            board.digital[pin].write(0)
            time.sleep(delay_sec)
            blinks += 1
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        board.digital[pin].write(0)
        board.exit()


def digital_write(pin=None, value=None, com_port=None):
    pin = _prompt_int(pin, "Enter the digital pin to write to: ")
    value = 1 if _prompt_int(value, "Enter the value (1 = HIGH, 0 = LOW): ") else 0
    com_port = _prompt_port(com_port)

    board = _connect(com_port)
    if board is None:
        return

    try:
        board.digital[pin].write(value)
        time.sleep(0.1)
        print(f"Pin {pin} set to {value}.")
    finally:
        board.exit()
