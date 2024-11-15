# ℹ️ Check out https://github.com/arunanshub/preload-rs for preload implemented in Rust

# preload

This preload is a clone of [Behdad Esfahbod's preload](http://preload.sf.net).
The only difference is that this project uses [`meson`](https://mesonbuild.com)
as its build system.

Note that this is a work in progress. So, if you're going to use it, make sure
that you check [`meson.build`](/meson.build) first.

Configuration file for `preload` is generated from buildfile (`meson.build`)
itself.

## Releases
![Build Status](https://copr.fedorainfracloud.org/coprs/kylegospo/preload/package/preload/status_image/last_build.png?)

You can get releases for Fedora from my [Copr](https://copr.fedorainfracloud.org/coprs/kylegospo/preload/).

## Building

It is highly recommended that you use `prefix` as `/usr`.

The proper way to build is:

```bash
meson build --prefix=/usr
# ...
ninja -C build
```

Even if you don't use `--prefix`, it is `/usr` by default.

### Manpage Generation

Optionally, you'd require `help2man` for dynamic manpage generation, which is
handled directly by Meson.

## Testing

Since `preload` is an executable, the tests are defined in a bash script
[`runtests.sh`](/runtests.sh), and are run via `meson`.

You can use

```sh
ninja -C build test
```

or

```sh
meson test -C build
```

to run the tests.

## Style Guide

[Chromium Style Guide](https://chromium.googlesource.com/chromium/src/+/HEAD/styleguide/c++/c++.md)
is used with some minor modifications:

- Maximum column length: 79
- Indent width: 4

Use this to generate a `.clang-format` file:

```bash
clang-format \
    -style="{BasedOnStyle: Chromium, ColumnLimit: 79, IndentWidth: 4}" \
    --dump-config > .clang-format
```

Check [Mesonbuild's guide on `clang-format`](https://mesonbuild.com/Code-formatting.html)
for more info.
