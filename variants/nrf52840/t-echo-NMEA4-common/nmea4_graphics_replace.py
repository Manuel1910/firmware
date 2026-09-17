Import("env")

from pathlib import Path

project_dir = Path(env.subst("$PROJECT_DIR")).resolve()

REPLACEMENTS = {
    "src/graphics/Screen.cpp":
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/Screen.cpp",
    "src/graphics/draw/UIRenderer.cpp":
        "variants/nrf52840/t-echo-NMEA4-common/src/graphics/draw/UIRenderer.cpp",
}

def nmea4_replace_graphics(env, node):
    try:
        node_path = Path(node.get_abspath()).resolve()
        rel = node_path.relative_to(project_dir).as_posix()
    except Exception:
        return node

    replacement = REPLACEMENTS.get(rel)
    if replacement is None:
        return node

    replacement_path = project_dir / replacement
    print("NMEA4: replace %s -> %s" % (rel, replacement))
    return env.File(str(replacement_path))

# PRE middleware is applied when PlatformIO constructs the build object nodes.
# We deliberately do not add the replacement Screen.cpp/UIRenderer.cpp again
# through build_src_filter; otherwise both originals and replacements could be built.
env.AddBuildMiddleware(nmea4_replace_graphics)
