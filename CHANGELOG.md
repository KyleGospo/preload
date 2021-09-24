## 0.1.0 (2021-09-24)

### Refactor

- **cmdline**: show package version
- **state**: rename `VERSION` to `PACKAGE_VERSION`
- **readahead**: mark unused field
- **cmdline**: remove redundant `const`s

### Fix

- **state**: use correct format code; don't use `__G_PRINTF_H__`
- **proc**: use correct format code; don't use `entry.d_name`

### Feat

- remove all build errors
- init