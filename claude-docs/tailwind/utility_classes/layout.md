# Layout

This document contains Tailwind CSS classes for Layout.

## aspect-ratio

Utilities for controlling the aspect ratio of an element.

### Classes

| Class | Styles |
| --- | --- |
| aspect-<ratio> | aspect-ratio: <ratio>; |
| aspect-square | aspect-ratio: 1 / 1; |
| aspect-video | aspect-ratio: var(--aspect-ratio-video); /* 16 / 9 */ |
| aspect-auto | aspect-ratio: auto; |
| aspect-(<custom-property>) | aspect-ratio: var(<custom-property>); |
| aspect-[<value>] | aspect-ratio: <value>; |

[Documentation](https://tailwindcss.com/docs/aspect-ratio)

---

## columns

Utilities for controlling the number of columns within an element.

### Classes

| Class | Styles |
| --- | --- |
| columns-<number> | columns: <number>; |
| columns-3xs | columns: var(--container-3xs); /* 16rem (256px) */ |
| columns-2xs | columns: var(--container-2xs); /* 18rem (288px) */ |
| columns-xs | columns: var(--container-xs); /* 20rem (320px) */ |
| columns-sm | columns: var(--container-sm); /* 24rem (384px) */ |
| columns-md | columns: var(--container-md); /* 28rem (448px) */ |
| columns-lg | columns: var(--container-lg); /* 32rem (512px) */ |
| columns-xl | columns: var(--container-xl); /* 36rem (576px) */ |
| columns-2xl | columns: var(--container-2xl); /* 42rem (672px) */ |
| columns-3xl | columns: var(--container-3xl); /* 48rem (768px) */ |
| columns-4xl | columns: var(--container-4xl); /* 56rem (896px) */ |
| columns-5xl | columns: var(--container-5xl); /* 64rem (1024px) */ |
| columns-6xl | columns: var(--container-6xl); /* 72rem (1152px) */ |
| columns-7xl | columns: var(--container-7xl); /* 80rem (1280px) */ |
| columns-auto | columns: auto; |
| columns-(<custom-property>) | columns: var(<custom-property>); |
| columns-[<value>] | columns: <value>; |

[Documentation](https://tailwindcss.com/docs/columns)

---

## break-after

Utilities for controlling how a column or page should break after an element.

### Classes

| Class | Styles |
| --- | --- |
| break-after-auto | break-after: auto; |
| break-after-avoid | break-after: avoid; |
| break-after-all | break-after: all; |
| break-after-avoid-page | break-after: avoid-page; |
| break-after-page | break-after: page; |
| break-after-left | break-after: left; |
| break-after-right | break-after: right; |
| break-after-column | break-after: column; |

[Documentation](https://tailwindcss.com/docs/break-after)

---

## break-before

Utilities for controlling how a column or page should break before an element.

### Classes

| Class | Styles |
| --- | --- |
| break-before-auto | break-before: auto; |
| break-before-avoid | break-before: avoid; |
| break-before-all | break-before: all; |
| break-before-avoid-page | break-before: avoid-page; |
| break-before-page | break-before: page; |
| break-before-left | break-before: left; |
| break-before-right | break-before: right; |
| break-before-column | break-before: column; |

[Documentation](https://tailwindcss.com/docs/break-before)

---

## break-inside

Utilities for controlling how a column or page should break within an element.

### Classes

| Class | Styles |
| --- | --- |
| break-inside-auto | break-inside: auto; |
| break-inside-avoid | break-inside: avoid; |
| break-inside-avoid-page | break-inside: avoid-page; |
| break-inside-avoid-column | break-inside: avoid-column; |

[Documentation](https://tailwindcss.com/docs/break-inside)

---

## box-decoration-break

Utilities for controlling how element fragments should be rendered across multiple lines, columns, or pages.

### Classes

| Class | Styles |
| --- | --- |
| box-decoration-clone | box-decoration-break: clone |
| box-decoration-slice | box-decoration-break: slice |

[Documentation](https://tailwindcss.com/docs/box-decoration-break)

---

## box-sizing

Utilities for controlling how the browser should calculate an element's total size.

### Classes

| Class | Styles |
| --- | --- |
| box-border | box-sizing: border-box |
| box-content | box-sizing: content-box |

[Documentation](https://tailwindcss.com/docs/box-sizing)

---

## display

Utilities for controlling the display box type of an element.

### Classes

| Class | Styles |
| --- | --- |
| inline | display: inline; |
| block | display: block; |
| inline-block | display: inline-block; |
| flow-root | display: flow-root; |
| flex | display: flex; |
| inline-flex | display: inline-flex; |
| grid | display: grid; |
| inline-grid | display: inline-grid; |
| contents | display: contents; |
| table | display: table; |
| inline-table | display: inline-table; |
| table-caption | display: table-caption; |
| table-cell | display: table-cell; |
| table-column | display: table-column; |
| table-column-group | display: table-column-group; |
| table-footer-group | display: table-footer-group; |
| table-header-group | display: table-header-group; |
| table-row-group | display: table-row-group; |
| table-row | display: table-row; |
| list-item | display: list-item; |
| hidden | display: none; |
| sr-only | position: absolute;<br>width: 1px;<br>height: 1px;<br>padding: 0;<br>margin: -1px;<br>overflow: hidden;<br>clip: rect(0, 0, 0, 0);<br>white-space: nowrap;<br>border-width: 0; |
| not-sr-only | position: static;<br>width: auto;<br>height: auto;<br>padding: 0;<br>margin: 0;<br>overflow: visible;<br>clip: auto;<br>white-space: normal; |

[Documentation](https://tailwindcss.com/docs/display)

---

## float

Utilities for controlling the wrapping of content around an element.

### Classes

| Class | Styles |
| --- | --- |
| float-right | float: right; |
| float-left | float: left; |
| float-start | float: inline-start; |
| float-end | float: inline-end; |
| float-none | float: none; |

[Documentation](https://tailwindcss.com/docs/float)

---

## clear

Utilities for controlling the wrapping of content around an element.

### Classes

| Class | Styles |
| --- | --- |
| clear-left | clear: left; |
| clear-right | clear: right; |
| clear-both | clear: both; |
| clear-start | clear: inline-start; |
| clear-end | clear: inline-end; |
| clear-none | clear: none; |

[Documentation](https://tailwindcss.com/docs/clear)

---

## isolation

Utilities for controlling whether an element should explicitly create a new stacking context.

### Classes

| Class | Styles |
| --- | --- |
| isolate | isolation: isolate; |
| isolation-auto | isolation: auto; |

[Documentation](https://tailwindcss.com/docs/isolation)

---

## object-fit

Utilities for controlling how a replaced element's content should be resized.

### Classes

| Class | Styles |
| --- | --- |
| object-contain | object-fit: contain; |
| object-cover | object-fit: cover; |
| object-fill | object-fit: fill; |
| object-none | object-fit: none; |
| object-scale-down | object-fit: scale-down; |

[Documentation](https://tailwindcss.com/docs/object-fit)

---

## object-position

Utilities for controlling how a replaced element's content should be positioned within its container.

### Classes

| Class | Styles |
| --- | --- |
| object-top-left | object-position: top left; |
| object-top | object-position: top; |
| object-top-right | object-position: top right; |
| object-left | object-position: left; |
| object-center | object-position: center; |
| object-right | object-position: right; |
| object-bottom-left | object-position: bottom left; |
| object-bottom | object-position: bottom; |
| object-bottom-right | object-position: bottom right; |
| object-(<custom-property>) | object-position: var(<custom-property>); |
| object-[<value>] | object-position: <value>; |

[Documentation](https://tailwindcss.com/docs/object-position)

---

## overflow

Utilities for controlling how an element handles content that is too large for the container.

### Classes

| Class | Styles |
| --- | --- |
| overflow-auto | overflow: auto; |
| overflow-hidden | overflow: hidden; |
| overflow-clip | overflow: clip; |
| overflow-visible | overflow: visible; |
| overflow-scroll | overflow: scroll; |
| overflow-x-auto | overflow-x: auto; |
| overflow-y-auto | overflow-y: auto; |
| overflow-x-hidden | overflow-x: hidden; |
| overflow-y-hidden | overflow-y: hidden; |
| overflow-x-clip | overflow-x: clip; |
| overflow-y-clip | overflow-y: clip; |
| overflow-x-visible | overflow-x: visible; |
| overflow-y-visible | overflow-y: visible; |
| overflow-x-scroll | overflow-x: scroll; |
| overflow-y-scroll | overflow-y: scroll; |

[Documentation](https://tailwindcss.com/docs/overflow)

---

## overscroll-behavior

Utilities for controlling how the browser behaves when reaching the boundary of a scrolling area.

### Classes

| Class | Styles |
| --- | --- |
| overscroll-auto | overscroll-behavior: auto; |
| overscroll-contain | overscroll-behavior: contain; |
| overscroll-none | overscroll-behavior: none; |
| overscroll-x-auto | overscroll-behavior-x: auto; |
| overscroll-x-contain | overscroll-behavior-x: contain; |
| overscroll-x-none | overscroll-behavior-x: none; |
| overscroll-y-auto | overscroll-behavior-y: auto; |
| overscroll-y-contain | overscroll-behavior-y: contain; |
| overscroll-y-none | overscroll-behavior-y: none; |

[Documentation](https://tailwindcss.com/docs/overscroll-behavior)

---

## position

Utilities for controlling how an element is positioned in the document.

### Classes

| Class | Styles |
| --- | --- |
| static | position: static; |
| fixed | position: fixed; |
| absolute | position: absolute; |
| relative | position: relative; |
| sticky | position: sticky; |

[Documentation](https://tailwindcss.com/docs/position)

---

## top / right / bottom / left

Utilities for controlling the placement of positioned elements.

### Classes

| Class | Styles |
| --- | --- |
| inset-<number> | inset: calc(var(--spacing) * <number>); |
| -inset-<number> | inset: calc(var(--spacing) * -<number>); |
| inset-<fraction> | inset: calc(<fraction> * 100%); |
| -inset-<fraction> | inset: calc(<fraction> * -100%); |
| inset-px | inset: 1px; |
| -inset-px | inset: -1px; |
| inset-full | inset: 100%; |
| -inset-full | inset: -100%; |
| inset-auto | inset: auto; |
| inset-(<custom-property>) | inset: var(<custom-property>); |
| inset-[<value>] | inset: <value>; |
| inset-x-<number> | inset-inline: calc(var(--spacing) * <number>); |
| -inset-x-<number> | inset-inline: calc(var(--spacing) * -<number>); |
| inset-x-<fraction> | inset-inline: calc(<fraction> * 100%); |
| -inset-x-<fraction> | inset-inline: calc(<fraction> * -100%); |
| inset-x-px | inset-inline: 1px; |
| -inset-x-px | inset-inline: -1px; |
| inset-x-full | inset-inline: 100%; |
| -inset-x-full | inset-inline: -100%; |
| inset-x-auto | inset-inline: auto; |
| inset-x-(<custom-property>) | inset-inline: var(<custom-property>); |
| inset-x-[<value>] | inset-inline: <value>; |
| inset-y-<number> | inset-block: calc(var(--spacing) * <number>); |
| -inset-y-<number> | inset-block: calc(var(--spacing) * -<number>); |
| inset-y-<fraction> | inset-block: calc(<fraction> * 100%); |
| -inset-y-<fraction> | inset-block: calc(<fraction> * -100%); |
| inset-y-px | inset-block: 1px; |
| -inset-y-px | inset-block: -1px; |
| inset-y-full | inset-block: 100%; |
| -inset-y-full | inset-block: -100%; |
| inset-y-auto | inset-block: auto; |
| inset-y-(<custom-property>) | inset-block: var(<custom-property>); |
| inset-y-[<value>] | inset-block: <value>; |
| start-<number> | inset-inline-start: calc(var(--spacing) * <number>); |
| -start-<number> | inset-inline-start: calc(var(--spacing) * -<number>); |
| start-<fraction> | inset-inline-start: calc(<fraction> * 100%); |
| -start-<fraction> | inset-inline-start: calc(<fraction> * -100%); |
| start-px | inset-inline-start: 1px; |
| -start-px | inset-inline-start: -1px; |
| start-full | inset-inline-start: 100%; |
| -start-full | inset-inline-start: -100%; |
| start-auto | inset-inline-start: auto; |
| start-(<custom-property>) | inset-inline-start: var(<custom-property>); |
| start-[<value>] | inset-inline-start: <value>; |
| end-<number> | inset-inline-end: calc(var(--spacing) * <number>); |
| -end-<number> | inset-inline-end: calc(var(--spacing) * -<number>); |
| end-<fraction> | inset-inline-end: calc(<fraction> * 100%); |
| -end-<fraction> | inset-inline-end: calc(<fraction> * -100%); |
| end-px | inset-inline-end: 1px; |
| -end-px | inset-inline-end: -1px; |
| end-full | inset-inline-end: 100%; |
| -end-full | inset-inline-end: -100%; |
| end-auto | inset-inline-end: auto; |
| end-(<custom-property>) | inset-inline-end: var(<custom-property>); |
| end-[<value>] | inset-inline-end: <value>; |
| top-<number> | top: calc(var(--spacing) * <number>); |
| -top-<number> | top: calc(var(--spacing) * -<number>); |
| top-<fraction> | top: calc(<fraction> * 100%); |
| -top-<fraction> | top: calc(<fraction> * -100%); |
| top-px | top: 1px; |
| -top-px | top: -1px; |
| top-full | top: 100%; |
| -top-full | top: -100%; |
| top-auto | top: auto; |
| top-(<custom-property>) | top: var(<custom-property>); |
| top-[<value>] | top: <value>; |
| right-<number> | right: calc(var(--spacing) * <number>); |
| -right-<number> | right: calc(var(--spacing) * -<number>); |
| right-<fraction> | right: calc(<fraction> * 100%); |
| -right-<fraction> | right: calc(<fraction> * -100%); |
| right-px | right: 1px; |
| -right-px | right: -1px; |
| right-full | right: 100%; |
| -right-full | right: -100%; |
| right-auto | right: auto; |
| right-(<custom-property>) | right: var(<custom-property>); |
| right-[<value>] | right: <value>; |
| bottom-<number> | bottom: calc(var(--spacing) * <number>); |
| -bottom-<number> | bottom: calc(var(--spacing) * -<number>); |
| bottom-<fraction> | bottom: calc(<fraction> * 100%); |
| -bottom-<fraction> | bottom: calc(<fraction> * -100%); |
| bottom-px | bottom: 1px; |
| -bottom-px | bottom: -1px; |
| bottom-full | bottom: 100%; |
| -bottom-full | bottom: -100%; |
| bottom-auto | bottom: auto; |
| bottom-(<custom-property>) | bottom: var(<custom-property>); |
| bottom-[<value>] | bottom: <value>; |
| left-<number> | left: calc(var(--spacing) * <number>); |
| -left-<number> | left: calc(var(--spacing) * -<number>); |
| left-<fraction> | left: calc(<fraction> * 100%); |
| -left-<fraction> | left: calc(<fraction> * -100%); |
| left-px | left: 1px; |
| -left-px | left: -1px; |
| left-full | left: 100%; |
| -left-full | left: -100%; |
| left-auto | left: auto; |
| left-(<custom-property>) | left: var(<custom-property>); |
| left-[<value>] | left: <value>; |

[Documentation](https://tailwindcss.com/docs/top-right-bottom-left)

---

## visibility

Utilities for controlling the visibility of an element.

### Classes

| Class | Styles |
| --- | --- |
| visible | visibility: visible; |
| invisible | visibility: hidden; |
| collapse | visibility: collapse; |

[Documentation](https://tailwindcss.com/docs/visibility)

---

## z-index

Utilities for controlling the stack order of an element.

### Classes

| Class | Styles |
| --- | --- |
| z-<number> | z-index: <number>; |
| z-auto | z-index: auto; |
| z-[<value>] | z-index: <value>; |
| z-(<custom-property>) | z-index: var(<custom-property>); |

[Documentation](https://tailwindcss.com/docs/z-index)

---

