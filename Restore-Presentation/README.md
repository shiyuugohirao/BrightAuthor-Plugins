# Restore Presentation

> [日本語版はこちら](README_ja.md)

## Overview

Returns to the previous presentation when switching among multiple linked presentations. Without this plugin, reliably returning to the prior presentation in a group of three or more requires complex conditional expressions and User Variables.

## Plugin Name

```
switch
```

## Installation

Add to **every** presentation in the group:

1. Download `Restore_Presentation.brs` from this folder.
2. In BrightAuthor, go to **File > Presentation Properties > Autorun**.
3. Click **Add Script Plugin** and select `Restore_Presentation.brs`.
4. Set the plugin **Name** to `switch`.
5. In **File > Presentation Properties > Switch Presentations**, add all other presentations in the group. Repeat for each presentation.

## Usage

### Save (before switching away)

Send a Plugin Message to the `switch` plugin:

```
save!<project_name>
```

Replace `<project_name>` with the presentation name to restore later.

### Restore (switch back)

```
restore
```

### Workflow

1. First presentation starts.
2. Plugin Message `save!<project_name>` is sent.
3. Switch Presentation command transitions to the next presentation.
4. Next presentation starts. Plugin Message `restore` switches back to the saved `<project_name>`.

### UDP Commands

| Command | Description |
|---------|-------------|
| `switch!save!<project_name>` | Save presentation name |
| `switch!restore` | Restore saved presentation |

## Related Files

| File | Description |
|------|-------------|
| `Restore_Presentation.brs` | Main plugin script |

## See Also

- [BrightSign Plugins and Parsers documentation](http://docs.brightsign.biz/display/DOC/BrightAuthor+Plugins+and+Parsers)
