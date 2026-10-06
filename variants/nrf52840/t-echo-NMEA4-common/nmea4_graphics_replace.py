Import("env")

# Replace ONLY the two existing Meshtastic translation units.
# Pattern-based matching follows PlatformIO's documented Build Middleware
# replacement mechanism and avoids adding a second Screen/UI object.

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
def replace_screen(env, node):
    replacement = env.File(
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/Screen.cpp"
    )
    print("NMEA4: replace src/graphics/Screen.cpp")
    return replacement

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
def replace_ui_renderer(env, node):
    replacement = env.File(
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/draw/UIRenderer.cpp"
    )
    print("NMEA4: replace src/graphics/draw/UIRenderer.cpp")
    return replacement

<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
=======
>>>>>>> fd5099a19be3e1de299944aaf49035f9e44e6c23
env.AddBuildMiddleware(replace_screen, "src/graphics/Screen.cpp")
env.AddBuildMiddleware(replace_ui_renderer, "src/graphics/draw/UIRenderer.cpp")
