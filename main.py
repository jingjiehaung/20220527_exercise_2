def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 0:
        pins.digital_write_pin(DigitalPin.P8, 0)
        pins.digital_write_pin(DigitalPin.P9, 1)
        pins.digital_write_pin(DigitalPin.P10, 0)
        pins.digital_write_pin(DigitalPin.P11, 1)
        basic.show_number(0)
    else:
        pins.digital_write_pin(DigitalPin.P8, 1)
        pins.digital_write_pin(DigitalPin.P9, 0)
        pins.digital_write_pin(DigitalPin.P10, 1)
        pins.digital_write_pin(DigitalPin.P11, 1)
        basic.show_number(1)
basic.forever(on_forever)
