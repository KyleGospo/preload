# preload

> This is currently a WIP

This preload is a clone of [Behdad Esfahbod's preload](http://preload.sf.net).
The only difference is that this project uses [`meson`](https://mesonbuild.com)
as its build system.

Note that this is a work in progress, and the entire codebase is in the root
directory instead of `src/`.

So, if you're going to use it, make sure that you check
[`meson.build`](/meson.build) first.

Configuration file for `preload` can be generated via:

```sh
./gen.preload.conf.sh preload.conf.in confkeys.in
```

Although there are better ways to do this, I'll simply leave it like this for
now.
