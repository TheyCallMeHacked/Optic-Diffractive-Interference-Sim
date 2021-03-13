#pragma once
#include <cmath>

float sqr(float x) {
    return x*x;
}

float map(float in, float min_in, float max_in, float min_out, float max_out) {
    float r(max_in - min_in), R(max_out - min_out), x(in - min_in);
    return (x*R/r) + min_out;
}

float sinc(float x) {
    return (x == 0) ? 1 : std::sin(x)/x;
}

float norm_sinc(float s, float w) {
    float scaler = ((1 + sinc(w)) < (2*sinc(w))) ? 2*sinc(w) : 1 + sinc(w);
    return (s/scaler > 1) ? 1 : (s/scaler < 0) ? -s/scaler : s/scaler;
}
