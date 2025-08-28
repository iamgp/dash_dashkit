# Callouts

Callout components for displaying important information with different styling variants. Perfect for highlighting notes, tips, warnings, and other important content.

## Overview

Callouts provide a consistent way to display contextual information with colored borders, icons, and semantic meaning. Each callout type uses specific colors and icons to communicate the urgency or type of information.

## Components

### Callout

The base callout component with configurable variants.

```python
from dashkit import Callout

# Basic usage
Callout("Your message here", variant="note")
```

**Props:**
- `children` (Any): Content to display inside the callout
- `variant` (Literal["note", "tip", "important", "warning", "caution"]): The type of callout (default: "note")
- `className` (str): Additional CSS classes (default: "")
- `**kwargs`: Additional props passed to the outer div

### Specialized Callouts

For convenience, we provide specialized callout components for each type:

#### NoteCallout
Blue callout for useful information that users should know.

```python
from dashkit import NoteCallout

NoteCallout("Useful information that users should know, even when skimming content.")
```

#### TipCallout
Green callout for helpful advice and pro tips.

```python
from dashkit import TipCallout

TipCallout([
    "Helpful advice for doing things better or more easily. ",
    html.Strong("Pro tip: "),
    "Use callouts sparingly to maintain their effectiveness."
])
```

#### ImportantCallout
Purple callout for key information users need to know.

```python
from dashkit import ImportantCallout

ImportantCallout("Key information users need to know to achieve their goal.")
```

#### WarningCallout
Amber/yellow callout for urgent information requiring immediate attention.

```python
from dashkit import WarningCallout

WarningCallout("Urgent info that needs immediate user attention to avoid problems.")
```

#### CautionCallout
Red callout for risks or negative outcomes.

```python
from dashkit import CautionCallout

CautionCallout([
    "Advises about risks or negative outcomes of certain actions. ",
    html.Strong("Be careful: "),
    "This action cannot be undone and may result in data loss."
])
```

## Examples

### Basic Usage

```python
from dashkit import NoteCallout, TipCallout, ImportantCallout, WarningCallout, CautionCallout

# Simple text
NoteCallout("This is a note with useful information.")

# With HTML elements
TipCallout([
    "You can use ",
    html.Strong("HTML elements"),
    " inside callouts for formatting."
])

# Custom styling
WarningCallout(
    "Custom warning with additional styling",
    className="my-4 shadow-lg"
)
```

### Mixed Content

```python
# Callouts can contain any Dash components
ImportantCallout([
    html.P("This callout contains multiple paragraphs."),
    html.P([
        "You can include ",
        html.A("links", href="#", className="text-purple-600 underline"),
        " and other interactive elements."
    ]),
    html.Ul([
        html.Li("List items work too"),
        html.Li("Making callouts very flexible")
    ], className="mt-2 ml-4")
])
```

## Styling

### Colors and Variants

Each callout type uses specific colors:

- **Note**: Blue (`text-blue-500`, `border-blue-500`)
- **Tip**: Green (`text-green-500`, `border-green-500`)
- **Important**: Purple (`text-purple-500`, `border-purple-500`)
- **Warning**: Amber (`text-amber-600`, `border-amber-500`)
- **Caution**: Red (`text-red-500`, `border-red-500`)

### Icons

Callouts use MynaUI icons via dash-iconify:

- **Note**: `mynaui:info-circle`
- **Tip**: `mynaui:danger-circle`
- **Important**: `mynaui:bookmark`
- **Warning**: `mynaui:danger-diamond`
- **Caution**: `mynaui:danger-hexagon`

### Dark Mode

All callouts automatically support dark mode with appropriate color adjustments for text and backgrounds.

### Customization

You can customize callouts by:

1. **Adding custom CSS classes:**
   ```python
   NoteCallout("Custom note", className="my-custom-class")
   ```

2. **Using the base Callout component for different styling:**
   ```python
   Callout("Custom callout", variant="note", className="border-2 shadow-xl")
   ```

## Best Practices

1. **Use sparingly** - Too many callouts can overwhelm users
2. **Choose the right type** - Match the semantic meaning to the content
3. **Keep content concise** - Callouts should highlight key information
4. **Consider placement** - Position callouts where they provide the most value
5. **Test accessibility** - Ensure sufficient color contrast and screen reader support

## Accessibility

- Icons are decorative and don't interfere with screen readers
- Color coding is supplemented with text labels (Note, Tip, etc.)
- Semantic HTML structure supports assistive technologies
- Sufficient color contrast in both light and dark modes