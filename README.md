# LSP-bash

Bash support for Sublime's LSP plugin provided through [bash-language-server](https://github.com/bash-lsp/bash-language-server).

## Installation

- Install [LSP](https://packagecontrol.io/packages/LSP) and [LSP-bash](https://packagecontrol.io/packages/LSP-bash) from Package Control.
- Restart Sublime.

## Configuration

There are some ways to configure the package and the language server.

- From `Preferences > Package Settings > LSP > Servers > LSP-bash`
- From the command palette `Preferences: LSP-bash Settings`

### Linting with `shellcheck`

In plugin settings,

```js
{
  "env": {
    // If you have shellcheck on your machine, you can provide its path here to do linting.
    // Or, if it can be found in PATH environment variable, you can simpliy use "shellcheck".
    // To download shellcheck, go https://github.com/koalaman/shellcheck/releases/latest
    "SHELLCHECK_PATH": "",
  },
}
```
