#pragma once
#include <OLEDDisplay.h>
#include <OLEDDisplayUi.h>
namespace graphics::SatellitesRenderer
{
void drawFrame(OLEDDisplay *display, OLEDDisplayUiState *state, int16_t x, int16_t y);
}
