images.arrow_image(ArrowNames.NORTH).show_image(0)
images.arrow_image(ArrowNames.NORTH_EAST).show_image(0)
images.arrow_image(ArrowNames.EAST).show_image(0)
images.arrow_image(ArrowNames.SOUTH_EAST).show_image(0)
images.arrow_image(ArrowNames.SOUTH).show_image(0)
images.arrow_image(ArrowNames.SOUTH_WEST).show_image(0)
images.arrow_image(ArrowNames.WEST).show_image(0)
images.arrow_image(ArrowNames.NORTH_WEST).show_image(0)
basic.show_leds("""
    . # . # .
        # # # # #
        # . . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . . . .
        . # . # .
        # # # # #
        # . . . #
        . # # # .
""")
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.SMALL_HEART)
myImage = images.create_image("""
    . . . . .
        . # . # .
        . . . . .
        . # # # .
        # . . . #
""")
myImage.show_image(0)
myImage = images.create_image("""
    . . . . .
        # # . # #
        . . . . #
        . # # # .
        # . . . #
""")
myImage.show_image(0)

def on_forever():
    pass
basic.forever(on_forever)
