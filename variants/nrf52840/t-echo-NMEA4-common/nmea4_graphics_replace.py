Import("env")

# Replace ONLY the two existing Meshtastic translation units.
# Pattern-based matching follows PlatformIO's documented Build Middleware
# replacement mechanism and avoids adding a second Screen/UI object.

def replace_screen(env, node):
    replacement = env.File(
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/Screen.cpp"
    )
    print("NMEA4: replace src/graphics/Screen.cpp")
    return replacement

def replace_ui_renderer(env, node):
    replacement = env.File(
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/draw/UIRenderer.cpp"
    )
    print("NMEA4: replace src/graphics/draw/UIRenderer.cpp")
    return replacement

env.AddBuildMiddleware(replace_screen, "src/graphics/Screen.cpp")
env.AddBuildMiddleware(replace_ui_renderer, "src/graphics/draw/UIRenderer.cpp")
