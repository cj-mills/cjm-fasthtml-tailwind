# Tables

This document contains Tailwind CSS classes for Tables.

## border-collapse

Utilities for controlling whether table borders should collapse or be separated.

### Classes

| Class | Styles |
| --- | --- |
| border-collapse | border-collapse: collapse; |
| border-separate | border-collapse: separate; |

[Documentation](https://tailwindcss.com/docs/border-collapse)

---

## border-spacing

Utilities for controlling the spacing between table borders.

### Classes

| Class | Styles |
| --- | --- |
| border-spacing-<number> | border-spacing: calc(var(--spacing) * <number>); |
| border-spacing-(<custom-property>) | border-spacing: var(<custom-property>); |
| border-spacing-[<value>] | border-spacing: <value>; |
| border-spacing-x-<number> | border-spacing: calc(var(--spacing) * <number>) var(--tw-border-spacing-y); |
| border-spacing-x-(<custom-property>) | border-spacing: var(<custom-property>) var(--tw-border-spacing-y); |
| border-spacing-x-[<value>] | border-spacing: <value> var(--tw-border-spacing-y); |
| border-spacing-y-<number> | border-spacing: var(--tw-border-spacing-x) calc(var(--spacing) * <number>); |
| border-spacing-y-(<custom-property>) | border-spacing: var(--tw-border-spacing-x) var(<custom-property>); |
| border-spacing-y-[<value>] | border-spacing: var(--tw-border-spacing-x) <value>; |

[Documentation](https://tailwindcss.com/docs/border-spacing)

---

## table-layout

Utilities for controlling the table layout algorithm.

### Classes

| Class | Styles |
| --- | --- |
| table-auto | table-layout: auto; |
| table-fixed | table-layout: fixed; |

[Documentation](https://tailwindcss.com/docs/table-layout)

---

## caption-side

Utilities for controlling the alignment of a caption element inside of a table.

### Classes

| Class | Styles |
| --- | --- |
| caption-top | caption-side: top; |
| caption-bottom | caption-side: bottom; |

[Documentation](https://tailwindcss.com/docs/caption-side)

---

