# Borders

This document contains Tailwind CSS classes for Borders.

## border-radius

Utilities for controlling the border radius of an element.

### Classes

| Class | Styles |
| --- | --- |
| rounded-xs | border-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-sm | border-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-md | border-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-lg | border-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-xl | border-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-2xl | border-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-3xl | border-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-4xl | border-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-none | border-radius: 0; |
| rounded-full | border-radius: calc(infinity * 1px); |
| rounded-(<custom-property>) | border-radius: var(<custom-property>); |
| rounded-[<value>] | border-radius: <value>; |
| rounded-s-xs | border-start-start-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-end-start-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-s-sm | border-start-start-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-end-start-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-s-md | border-start-start-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-end-start-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-s-lg | border-start-start-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-end-start-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-s-xl | border-start-start-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-end-start-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-s-2xl | border-start-start-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-end-start-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-s-3xl | border-start-start-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-end-start-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-s-4xl | border-start-start-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-end-start-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-s-none | border-start-start-radius: 0;<br>border-end-start-radius: 0; |
| rounded-s-full | border-start-start-radius: calc(infinity * 1px);<br>border-end-start-radius: calc(infinity * 1px); |
| rounded-s-(<custom-property>) | border-start-start-radius: var(<br><custom-property><br>);<br>border-end-start-radius: var(<br><custom-property><br>); |
| rounded-s-[<value>] | border-start-start-radius: <br><value><br>;<br>border-end-start-radius: <br><value><br>; |
| rounded-e-xs | border-start-end-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-end-end-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-e-sm | border-start-end-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-end-end-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-e-md | border-start-end-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-end-end-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-e-lg | border-start-end-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-end-end-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-e-xl | border-start-end-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-end-end-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-e-2xl | border-start-end-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-end-end-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-e-3xl | border-start-end-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-end-end-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-e-4xl | border-start-end-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-end-end-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-e-none | border-start-end-radius: 0;<br>border-end-end-radius: 0; |
| rounded-e-full | border-start-end-radius: calc(infinity * 1px);<br>border-end-end-radius: calc(infinity * 1px); |
| rounded-e-(<custom-property>) | border-start-end-radius: var(<br><custom-property><br>);<br>border-end-end-radius: var(<br><custom-property><br>); |
| rounded-e-[<value>] | border-start-end-radius: <br><value><br>;<br>border-end-end-radius: <br><value><br>; |
| rounded-t-xs | border-top-left-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-top-right-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-t-sm | border-top-left-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-top-right-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-t-md | border-top-left-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-top-right-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-t-lg | border-top-left-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-top-right-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-t-xl | border-top-left-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-top-right-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-t-2xl | border-top-left-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-top-right-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-t-3xl | border-top-left-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-top-right-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-t-4xl | border-top-left-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-top-right-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-t-none | border-top-left-radius: 0;<br>border-top-right-radius: 0; |
| rounded-t-full | border-top-left-radius: calc(infinity * 1px);<br>border-top-right-radius: calc(infinity * 1px); |
| rounded-t-(<custom-property>) | border-top-left-radius: var(<br><custom-property><br>);<br>border-top-right-radius: var(<br><custom-property><br>); |
| rounded-t-[<value>] | border-top-left-radius: <br><value><br>;<br>border-top-right-radius: <br><value><br>; |
| rounded-r-xs | border-top-right-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-bottom-right-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-r-sm | border-top-right-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-bottom-right-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-r-md | border-top-right-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-bottom-right-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-r-lg | border-top-right-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-bottom-right-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-r-xl | border-top-right-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-bottom-right-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-r-2xl | border-top-right-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-bottom-right-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-r-3xl | border-top-right-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-bottom-right-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-r-4xl | border-top-right-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-bottom-right-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-r-none | border-top-right-radius: 0;<br>border-bottom-right-radius: 0; |
| rounded-r-full | border-top-right-radius: calc(infinity * 1px);<br>border-bottom-right-radius: calc(infinity * 1px); |
| rounded-r-(<custom-property>) | border-top-right-radius: var(<br><custom-property><br>);<br>border-bottom-right-radius: var(<br><custom-property><br>); |
| rounded-r-[<value>] | border-top-right-radius: <br><value><br>;<br>border-bottom-right-radius: <br><value><br>; |
| rounded-b-xs | border-bottom-right-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-bottom-left-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-b-sm | border-bottom-right-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-bottom-left-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-b-md | border-bottom-right-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-bottom-left-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-b-lg | border-bottom-right-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-bottom-left-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-b-xl | border-bottom-right-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-bottom-left-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-b-2xl | border-bottom-right-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-bottom-left-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-b-3xl | border-bottom-right-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-bottom-left-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-b-4xl | border-bottom-right-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-bottom-left-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-b-none | border-bottom-right-radius: 0;<br>border-bottom-left-radius: 0; |
| rounded-b-full | border-bottom-right-radius: calc(infinity * 1px);<br>border-bottom-left-radius: calc(infinity * 1px); |
| rounded-b-(<custom-property>) | border-bottom-right-radius: var(<br><custom-property><br>);<br>border-bottom-left-radius: var(<br><custom-property><br>); |
| rounded-b-[<value>] | border-bottom-right-radius: <br><value><br>;<br>border-bottom-left-radius: <br><value><br>; |
| rounded-l-xs | border-top-left-radius: var(--radius-xs); <br>/* 0.125rem (2px) */<br><br>border-bottom-left-radius: var(--radius-xs); <br>/* 0.125rem (2px) */ |
| rounded-l-sm | border-top-left-radius: var(--radius-sm); <br>/* 0.25rem (4px) */<br><br>border-bottom-left-radius: var(--radius-sm); <br>/* 0.25rem (4px) */ |
| rounded-l-md | border-top-left-radius: var(--radius-md); <br>/* 0.375rem (6px) */<br><br>border-bottom-left-radius: var(--radius-md); <br>/* 0.375rem (6px) */ |
| rounded-l-lg | border-top-left-radius: var(--radius-lg); <br>/* 0.5rem (8px) */<br><br>border-bottom-left-radius: var(--radius-lg); <br>/* 0.5rem (8px) */ |
| rounded-l-xl | border-top-left-radius: var(--radius-xl); <br>/* 0.75rem (12px) */<br><br>border-bottom-left-radius: var(--radius-xl); <br>/* 0.75rem (12px) */ |
| rounded-l-2xl | border-top-left-radius: var(--radius-2xl); <br>/* 1rem (16px) */<br><br>border-bottom-left-radius: var(--radius-2xl); <br>/* 1rem (16px) */ |
| rounded-l-3xl | border-top-left-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */<br><br>border-bottom-left-radius: var(--radius-3xl); <br>/* 1.5rem (24px) */ |
| rounded-l-4xl | border-top-left-radius: var(--radius-4xl); <br>/* 2rem (32px) */<br><br>border-bottom-left-radius: var(--radius-4xl); <br>/* 2rem (32px) */ |
| rounded-l-none | border-top-left-radius: 0;<br>border-bottom-left-radius: 0; |
| rounded-l-full | border-top-left-radius: calc(infinity * 1px);<br>border-bottom-left-radius: calc(infinity * 1px); |
| rounded-l-(<custom-property>) | border-top-left-radius: var(<br><custom-property><br>);<br>border-bottom-left-radius: var(<br><custom-property><br>); |
| rounded-l-[<value>] | border-top-left-radius: <br><value><br>;<br>border-bottom-left-radius: <br><value><br>; |
| rounded-ss-xs | border-start-start-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-ss-sm | border-start-start-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-ss-md | border-start-start-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-ss-lg | border-start-start-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-ss-xl | border-start-start-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-ss-2xl | border-start-start-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-ss-3xl | border-start-start-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-ss-4xl | border-start-start-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-ss-none | border-start-start-radius: 0; |
| rounded-ss-full | border-start-start-radius: calc(infinity * 1px); |
| rounded-ss-(<custom-property>) | border-start-start-radius: var(<custom-property>); |
| rounded-ss-[<value>] | border-start-start-radius: <value>; |
| rounded-se-xs | border-start-end-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-se-sm | border-start-end-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-se-md | border-start-end-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-se-lg | border-start-end-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-se-xl | border-start-end-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-se-2xl | border-start-end-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-se-3xl | border-start-end-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-se-4xl | border-start-end-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-se-none | border-start-end-radius: 0; |
| rounded-se-full | border-start-end-radius: calc(infinity * 1px); |
| rounded-se-(<custom-property>) | border-start-end-radius: var(<custom-property>); |
| rounded-se-[<value>] | border-start-end-radius: <value>; |
| rounded-ee-xs | border-end-end-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-ee-sm | border-end-end-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-ee-md | border-end-end-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-ee-lg | border-end-end-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-ee-xl | border-end-end-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-ee-2xl | border-end-end-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-ee-3xl | border-end-end-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-ee-4xl | border-end-end-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-ee-none | border-end-end-radius: 0; |
| rounded-ee-full | border-end-end-radius: calc(infinity * 1px); |
| rounded-ee-(<custom-property>) | border-end-end-radius: var(<custom-property>); |
| rounded-ee-[<value>] | border-end-end-radius: <value>; |
| rounded-es-xs | border-end-start-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-es-sm | border-end-start-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-es-md | border-end-start-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-es-lg | border-end-start-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-es-xl | border-end-start-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-es-2xl | border-end-start-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-es-3xl | border-end-start-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-es-4xl | border-end-start-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-es-none | border-end-start-radius: 0; |
| rounded-es-full | border-end-start-radius: calc(infinity * 1px); |
| rounded-es-(<custom-property>) | border-end-start-radius: var(<custom-property>); |
| rounded-es-[<value>] | border-end-start-radius: <value>; |
| rounded-tl-xs | border-top-left-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-tl-sm | border-top-left-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-tl-md | border-top-left-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-tl-lg | border-top-left-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-tl-xl | border-top-left-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-tl-2xl | border-top-left-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-tl-3xl | border-top-left-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-tl-4xl | border-top-left-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-tl-none | border-top-left-radius: 0; |
| rounded-tl-full | border-top-left-radius: calc(infinity * 1px); |
| rounded-tl-(<custom-property>) | border-top-left-radius: var(<custom-property>); |
| rounded-tl-[<value>] | border-top-left-radius: <value>; |
| rounded-tr-xs | border-top-right-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-tr-sm | border-top-right-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-tr-md | border-top-right-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-tr-lg | border-top-right-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-tr-xl | border-top-right-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-tr-2xl | border-top-right-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-tr-3xl | border-top-right-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-tr-4xl | border-top-right-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-tr-none | border-top-right-radius: 0; |
| rounded-tr-full | border-top-right-radius: calc(infinity * 1px); |
| rounded-tr-(<custom-property>) | border-top-right-radius: var(<custom-property>); |
| rounded-tr-[<value>] | border-top-right-radius: <value>; |
| rounded-br-xs | border-bottom-right-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-br-sm | border-bottom-right-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-br-md | border-bottom-right-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-br-lg | border-bottom-right-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-br-xl | border-bottom-right-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-br-2xl | border-bottom-right-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-br-3xl | border-bottom-right-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-br-4xl | border-bottom-right-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-br-none | border-bottom-right-radius: 0; |
| rounded-br-full | border-bottom-right-radius: calc(infinity * 1px); |
| rounded-br-(<custom-property>) | border-bottom-right-radius: var(<custom-property>); |
| rounded-br-[<value>] | border-bottom-right-radius: <value>; |
| rounded-bl-xs | border-bottom-left-radius: var(--radius-xs); /* 0.125rem (2px) */ |
| rounded-bl-sm | border-bottom-left-radius: var(--radius-sm); /* 0.25rem (4px) */ |
| rounded-bl-md | border-bottom-left-radius: var(--radius-md); /* 0.375rem (6px) */ |
| rounded-bl-lg | border-bottom-left-radius: var(--radius-lg); /* 0.5rem (8px) */ |
| rounded-bl-xl | border-bottom-left-radius: var(--radius-xl); /* 0.75rem (12px) */ |
| rounded-bl-2xl | border-bottom-left-radius: var(--radius-2xl); /* 1rem (16px) */ |
| rounded-bl-3xl | border-bottom-left-radius: var(--radius-3xl); /* 1.5rem (24px) */ |
| rounded-bl-4xl | border-bottom-left-radius: var(--radius-4xl); /* 2rem (32px) */ |
| rounded-bl-none | border-bottom-left-radius: 0; |
| rounded-bl-full | border-bottom-left-radius: calc(infinity * 1px); |
| rounded-bl-(<custom-property>) | border-bottom-left-radius: var(<custom-property>); |
| rounded-bl-[<value>] | border-bottom-left-radius: <value>; |

[Documentation](https://tailwindcss.com/docs/border-radius)

---

## border-width

Utilities for controlling the width of an element's borders.

### Classes

| Class | Styles |
| --- | --- |
| border | border-width: 1px; |
| border-<number> | border-width: <number>px; |
| border-(length:<custom-property>) | border-width: var(<custom-property>); |
| border-[<value>] | border-width: <value>; |
| border-x | border-inline-width: 1px; |
| border-x-<number> | border-inline-width: <number>px; |
| border-x-(length:<custom-property>) | border-inline-width: var(<custom-property>); |
| border-x-[<value>] | border-inline-width: <value>; |
| border-y | border-block-width: 1px; |
| border-y-<number> | border-block-width: <number>px; |
| border-y-(length:<custom-property>) | border-block-width: var(<custom-property>); |
| border-y-[<value>] | border-block-width: <value>; |
| border-s | border-inline-start-width: 1px; |
| border-s-<number> | border-inline-start-width: <number>px; |
| border-s-(length:<custom-property>) | border-inline-start-width: var(<custom-property>); |
| border-s-[<value>] | border-inline-start-width: <value>; |
| border-e | border-inline-end-width: 1px; |
| border-e-<number> | border-inline-end-width: <number>px; |
| border-e-(length:<custom-property>) | border-inline-end-width: var(<custom-property>); |
| border-e-[<value>] | border-inline-end-width: <value>; |
| border-t | border-top-width: 1px; |
| border-t-<number> | border-top-width: <number>px; |
| border-t-(length:<custom-property>) | border-top-width: var(<custom-property>); |
| border-t-[<value>] | border-top-width: <value>; |
| border-r | border-right-width: 1px; |
| border-r-<number> | border-right-width: <number>px; |
| border-r-(length:<custom-property>) | border-right-width: var(<custom-property>); |
| border-r-[<value>] | border-right-width: <value>; |
| border-b | border-bottom-width: 1px; |
| border-b-<number> | border-bottom-width: <number>px; |
| border-b-(length:<custom-property>) | border-bottom-width: var(<custom-property>); |
| border-b-[<value>] | border-bottom-width: <value>; |
| border-l | border-left-width: 1px; |
| border-l-<number> | border-left-width: <number>px; |
| border-l-(length:<custom-property>) | border-left-width: var(<custom-property>); |
| border-l-[<value>] | border-left-width: <value>; |
| divide-x | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: 1px;<br>} |
| divide-x-<number> | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: <br><number><br>px;<br>} |
| divide-x-(length:<custom-property>) | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: var(<br><custom-property><br>);<br>} |
| divide-x-[<value>] | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: <br><value><br>;<br>} |
| divide-y | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: 1px;<br>} |
| divide-y-<number> | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: <br><number><br>px;<br>} |
| divide-y-(length:<custom-property>) | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: var(<br><custom-property><br>);<br>} |
| divide-y-[<value>] | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: <br><value><br>;<br>} |
| divide-x-reverse | --tw-divide-x-reverse: 1; |
| divide-y-reverse | --tw-divide-y-reverse: 1; |

[Documentation](https://tailwindcss.com/docs/border-width)

---

## border-color

Utilities for controlling the color of an element's borders.

### Classes

| Class | Styles |
| --- | --- |
| border-inherit | border-color: inherit; |
| border-current | border-color: currentColor; |
| border-transparent | border-color: transparent; |
| border-black | border-color: var(--color-black); /* #000 */ |
| border-white | border-color: var(--color-white); /* #fff */ |
| border-red-50 | border-color: var(--color-red-50); |
| border-red-100 | border-color: var(--color-red-100); |
| border-red-200 | border-color: var(--color-red-200); |
| border-red-300 | border-color: var(--color-red-300); |
| border-red-400 | border-color: var(--color-red-400); |
| border-red-500 | border-color: var(--color-red-500); |
| border-red-600 | border-color: var(--color-red-600); |
| border-red-700 | border-color: var(--color-red-700); |
| border-red-800 | border-color: var(--color-red-800); |
| border-red-900 | border-color: var(--color-red-900); |
| border-red-950 | border-color: var(--color-red-950); |
| border-orange-50 | border-color: var(--color-orange-50); |
| border-orange-100 | border-color: var(--color-orange-100); |
| border-orange-200 | border-color: var(--color-orange-200); |
| border-orange-300 | border-color: var(--color-orange-300); |
| border-orange-400 | border-color: var(--color-orange-400); |
| border-orange-500 | border-color: var(--color-orange-500); |
| border-orange-600 | border-color: var(--color-orange-600); |
| border-orange-700 | border-color: var(--color-orange-700); |
| border-orange-800 | border-color: var(--color-orange-800); |
| border-orange-900 | border-color: var(--color-orange-900); |
| border-orange-950 | border-color: var(--color-orange-950); |
| border-amber-50 | border-color: var(--color-amber-50); |
| border-amber-100 | border-color: var(--color-amber-100); |
| border-amber-200 | border-color: var(--color-amber-200); |
| border-amber-300 | border-color: var(--color-amber-300); |
| border-amber-400 | border-color: var(--color-amber-400); |
| border-amber-500 | border-color: var(--color-amber-500); |
| border-amber-600 | border-color: var(--color-amber-600); |
| border-amber-700 | border-color: var(--color-amber-700); |
| border-amber-800 | border-color: var(--color-amber-800); |
| border-amber-900 | border-color: var(--color-amber-900); |
| border-amber-950 | border-color: var(--color-amber-950); |
| border-yellow-50 | border-color: var(--color-yellow-50); |
| border-yellow-100 | border-color: var(--color-yellow-100); |
| border-yellow-200 | border-color: var(--color-yellow-200); |
| border-yellow-300 | border-color: var(--color-yellow-300); |
| border-yellow-400 | border-color: var(--color-yellow-400); |
| border-yellow-500 | border-color: var(--color-yellow-500); |
| border-yellow-600 | border-color: var(--color-yellow-600); |
| border-yellow-700 | border-color: var(--color-yellow-700); |
| border-yellow-800 | border-color: var(--color-yellow-800); |
| border-yellow-900 | border-color: var(--color-yellow-900); |
| border-yellow-950 | border-color: var(--color-yellow-950); |
| border-lime-50 | border-color: var(--color-lime-50); |
| border-lime-100 | border-color: var(--color-lime-100); |
| border-lime-200 | border-color: var(--color-lime-200); |
| border-lime-300 | border-color: var(--color-lime-300); |
| border-lime-400 | border-color: var(--color-lime-400); |
| border-lime-500 | border-color: var(--color-lime-500); |
| border-lime-600 | border-color: var(--color-lime-600); |
| border-lime-700 | border-color: var(--color-lime-700); |
| border-lime-800 | border-color: var(--color-lime-800); |
| border-lime-900 | border-color: var(--color-lime-900); |
| border-lime-950 | border-color: var(--color-lime-950); |
| border-green-50 | border-color: var(--color-green-50); |
| border-green-100 | border-color: var(--color-green-100); |
| border-green-200 | border-color: var(--color-green-200); |
| border-green-300 | border-color: var(--color-green-300); |
| border-green-400 | border-color: var(--color-green-400); |
| border-green-500 | border-color: var(--color-green-500); |
| border-green-600 | border-color: var(--color-green-600); |
| border-green-700 | border-color: var(--color-green-700); |
| border-green-800 | border-color: var(--color-green-800); |
| border-green-900 | border-color: var(--color-green-900); |
| border-green-950 | border-color: var(--color-green-950); |
| border-emerald-50 | border-color: var(--color-emerald-50); |
| border-emerald-100 | border-color: var(--color-emerald-100); |
| border-emerald-200 | border-color: var(--color-emerald-200); |
| border-emerald-300 | border-color: var(--color-emerald-300); |
| border-emerald-400 | border-color: var(--color-emerald-400); |
| border-emerald-500 | border-color: var(--color-emerald-500); |
| border-emerald-600 | border-color: var(--color-emerald-600); |
| border-emerald-700 | border-color: var(--color-emerald-700); |
| border-emerald-800 | border-color: var(--color-emerald-800); |
| border-emerald-900 | border-color: var(--color-emerald-900); |
| border-emerald-950 | border-color: var(--color-emerald-950); |
| border-teal-50 | border-color: var(--color-teal-50); |
| border-teal-100 | border-color: var(--color-teal-100); |
| border-teal-200 | border-color: var(--color-teal-200); |
| border-teal-300 | border-color: var(--color-teal-300); |
| border-teal-400 | border-color: var(--color-teal-400); |
| border-teal-500 | border-color: var(--color-teal-500); |
| border-teal-600 | border-color: var(--color-teal-600); |
| border-teal-700 | border-color: var(--color-teal-700); |
| border-teal-800 | border-color: var(--color-teal-800); |
| border-teal-900 | border-color: var(--color-teal-900); |
| border-teal-950 | border-color: var(--color-teal-950); |
| border-cyan-50 | border-color: var(--color-cyan-50); |
| border-cyan-100 | border-color: var(--color-cyan-100); |
| border-cyan-200 | border-color: var(--color-cyan-200); |
| border-cyan-300 | border-color: var(--color-cyan-300); |
| border-cyan-400 | border-color: var(--color-cyan-400); |
| border-cyan-500 | border-color: var(--color-cyan-500); |
| border-cyan-600 | border-color: var(--color-cyan-600); |
| border-cyan-700 | border-color: var(--color-cyan-700); |
| border-cyan-800 | border-color: var(--color-cyan-800); |
| border-cyan-900 | border-color: var(--color-cyan-900); |
| border-cyan-950 | border-color: var(--color-cyan-950); |
| border-sky-50 | border-color: var(--color-sky-50); |
| border-sky-100 | border-color: var(--color-sky-100); |
| border-sky-200 | border-color: var(--color-sky-200); |
| border-sky-300 | border-color: var(--color-sky-300); |
| border-sky-400 | border-color: var(--color-sky-400); |
| border-sky-500 | border-color: var(--color-sky-500); |
| border-sky-600 | border-color: var(--color-sky-600); |
| border-sky-700 | border-color: var(--color-sky-700); |
| border-sky-800 | border-color: var(--color-sky-800); |
| border-sky-900 | border-color: var(--color-sky-900); |
| border-sky-950 | border-color: var(--color-sky-950); |
| border-blue-50 | border-color: var(--color-blue-50); |
| border-blue-100 | border-color: var(--color-blue-100); |
| border-blue-200 | border-color: var(--color-blue-200); |
| border-blue-300 | border-color: var(--color-blue-300); |
| border-blue-400 | border-color: var(--color-blue-400); |
| border-blue-500 | border-color: var(--color-blue-500); |
| border-blue-600 | border-color: var(--color-blue-600); |
| border-blue-700 | border-color: var(--color-blue-700); |
| border-blue-800 | border-color: var(--color-blue-800); |
| border-blue-900 | border-color: var(--color-blue-900); |
| border-blue-950 | border-color: var(--color-blue-950); |
| border-indigo-50 | border-color: var(--color-indigo-50); |
| border-indigo-100 | border-color: var(--color-indigo-100); |
| border-indigo-200 | border-color: var(--color-indigo-200); |
| border-indigo-300 | border-color: var(--color-indigo-300); |
| border-indigo-400 | border-color: var(--color-indigo-400); |
| border-indigo-500 | border-color: var(--color-indigo-500); |
| border-indigo-600 | border-color: var(--color-indigo-600); |
| border-indigo-700 | border-color: var(--color-indigo-700); |
| border-indigo-800 | border-color: var(--color-indigo-800); |
| border-indigo-900 | border-color: var(--color-indigo-900); |
| border-indigo-950 | border-color: var(--color-indigo-950); |
| border-violet-50 | border-color: var(--color-violet-50); |
| border-violet-100 | border-color: var(--color-violet-100); |
| border-violet-200 | border-color: var(--color-violet-200); |
| border-violet-300 | border-color: var(--color-violet-300); |
| border-violet-400 | border-color: var(--color-violet-400); |
| border-violet-500 | border-color: var(--color-violet-500); |
| border-violet-600 | border-color: var(--color-violet-600); |
| border-violet-700 | border-color: var(--color-violet-700); |
| border-violet-800 | border-color: var(--color-violet-800); |
| border-violet-900 | border-color: var(--color-violet-900); |
| border-violet-950 | border-color: var(--color-violet-950); |
| border-purple-50 | border-color: var(--color-purple-50); |
| border-purple-100 | border-color: var(--color-purple-100); |
| border-purple-200 | border-color: var(--color-purple-200); |
| border-purple-300 | border-color: var(--color-purple-300); |
| border-purple-400 | border-color: var(--color-purple-400); |
| border-purple-500 | border-color: var(--color-purple-500); |
| border-purple-600 | border-color: var(--color-purple-600); |
| border-purple-700 | border-color: var(--color-purple-700); |
| border-purple-800 | border-color: var(--color-purple-800); |
| border-purple-900 | border-color: var(--color-purple-900); |
| border-purple-950 | border-color: var(--color-purple-950); |
| border-fuchsia-50 | border-color: var(--color-fuchsia-50); |
| border-fuchsia-100 | border-color: var(--color-fuchsia-100); |
| border-fuchsia-200 | border-color: var(--color-fuchsia-200); |
| border-fuchsia-300 | border-color: var(--color-fuchsia-300); |
| border-fuchsia-400 | border-color: var(--color-fuchsia-400); |
| border-fuchsia-500 | border-color: var(--color-fuchsia-500); |
| border-fuchsia-600 | border-color: var(--color-fuchsia-600); |
| border-fuchsia-700 | border-color: var(--color-fuchsia-700); |
| border-fuchsia-800 | border-color: var(--color-fuchsia-800); |
| border-fuchsia-900 | border-color: var(--color-fuchsia-900); |
| border-fuchsia-950 | border-color: var(--color-fuchsia-950); |
| border-pink-50 | border-color: var(--color-pink-50); |
| border-pink-100 | border-color: var(--color-pink-100); |
| border-pink-200 | border-color: var(--color-pink-200); |
| border-pink-300 | border-color: var(--color-pink-300); |
| border-pink-400 | border-color: var(--color-pink-400); |
| border-pink-500 | border-color: var(--color-pink-500); |
| border-pink-600 | border-color: var(--color-pink-600); |
| border-pink-700 | border-color: var(--color-pink-700); |
| border-pink-800 | border-color: var(--color-pink-800); |
| border-pink-900 | border-color: var(--color-pink-900); |
| border-pink-950 | border-color: var(--color-pink-950); |
| border-rose-50 | border-color: var(--color-rose-50); |
| border-rose-100 | border-color: var(--color-rose-100); |
| border-rose-200 | border-color: var(--color-rose-200); |
| border-rose-300 | border-color: var(--color-rose-300); |
| border-rose-400 | border-color: var(--color-rose-400); |
| border-rose-500 | border-color: var(--color-rose-500); |
| border-rose-600 | border-color: var(--color-rose-600); |
| border-rose-700 | border-color: var(--color-rose-700); |
| border-rose-800 | border-color: var(--color-rose-800); |
| border-rose-900 | border-color: var(--color-rose-900); |
| border-rose-950 | border-color: var(--color-rose-950); |
| border-slate-50 | border-color: var(--color-slate-50); |
| border-slate-100 | border-color: var(--color-slate-100); |
| border-slate-200 | border-color: var(--color-slate-200); |
| border-slate-300 | border-color: var(--color-slate-300); |
| border-slate-400 | border-color: var(--color-slate-400); |
| border-slate-500 | border-color: var(--color-slate-500); |
| border-slate-600 | border-color: var(--color-slate-600); |
| border-slate-700 | border-color: var(--color-slate-700); |
| border-slate-800 | border-color: var(--color-slate-800); |
| border-slate-900 | border-color: var(--color-slate-900); |
| border-slate-950 | border-color: var(--color-slate-950); |
| border-gray-50 | border-color: var(--color-gray-50); |
| border-gray-100 | border-color: var(--color-gray-100); |
| border-gray-200 | border-color: var(--color-gray-200); |
| border-gray-300 | border-color: var(--color-gray-300); |
| border-gray-400 | border-color: var(--color-gray-400); |
| border-gray-500 | border-color: var(--color-gray-500); |
| border-gray-600 | border-color: var(--color-gray-600); |
| border-gray-700 | border-color: var(--color-gray-700); |
| border-gray-800 | border-color: var(--color-gray-800); |
| border-gray-900 | border-color: var(--color-gray-900); |
| border-gray-950 | border-color: var(--color-gray-950); |
| border-zinc-50 | border-color: var(--color-zinc-50); |
| border-zinc-100 | border-color: var(--color-zinc-100); |
| border-zinc-200 | border-color: var(--color-zinc-200); |
| border-zinc-300 | border-color: var(--color-zinc-300); |
| border-zinc-400 | border-color: var(--color-zinc-400); |
| border-zinc-500 | border-color: var(--color-zinc-500); |
| border-zinc-600 | border-color: var(--color-zinc-600); |
| border-zinc-700 | border-color: var(--color-zinc-700); |
| border-zinc-800 | border-color: var(--color-zinc-800); |
| border-zinc-900 | border-color: var(--color-zinc-900); |
| border-zinc-950 | border-color: var(--color-zinc-950); |
| border-neutral-50 | border-color: var(--color-neutral-50); |
| border-neutral-100 | border-color: var(--color-neutral-100); |
| border-neutral-200 | border-color: var(--color-neutral-200); |
| border-neutral-300 | border-color: var(--color-neutral-300); |
| border-neutral-400 | border-color: var(--color-neutral-400); |
| border-neutral-500 | border-color: var(--color-neutral-500); |
| border-neutral-600 | border-color: var(--color-neutral-600); |
| border-neutral-700 | border-color: var(--color-neutral-700); |
| border-neutral-800 | border-color: var(--color-neutral-800); |
| border-neutral-900 | border-color: var(--color-neutral-900); |
| border-neutral-950 | border-color: var(--color-neutral-950); |
| border-stone-50 | border-color: var(--color-stone-50); |
| border-stone-100 | border-color: var(--color-stone-100); |
| border-stone-200 | border-color: var(--color-stone-200); |
| border-stone-300 | border-color: var(--color-stone-300); |
| border-stone-400 | border-color: var(--color-stone-400); |
| border-stone-500 | border-color: var(--color-stone-500); |
| border-stone-600 | border-color: var(--color-stone-600); |
| border-stone-700 | border-color: var(--color-stone-700); |
| border-stone-800 | border-color: var(--color-stone-800); |
| border-stone-900 | border-color: var(--color-stone-900); |
| border-stone-950 | border-color: var(--color-stone-950); |
| border-(<custom-property>) | border-color: var(<custom-property>); |
| border-[<value>] | border-color: <value>; |
| border-x-inherit | border-inline-color: inherit; |
| border-x-current | border-inline-color: currentColor; |
| border-x-transparent | border-inline-color: transparent; |
| border-x-black | border-inline-color: var(--color-black); /* #000 */ |
| border-x-white | border-inline-color: var(--color-white); /* #fff */ |
| border-x-red-50 | border-inline-color: var(--color-red-50); |
| border-x-red-100 | border-inline-color: var(--color-red-100); |
| border-x-red-200 | border-inline-color: var(--color-red-200); |
| border-x-red-300 | border-inline-color: var(--color-red-300); |
| border-x-red-400 | border-inline-color: var(--color-red-400); |
| border-x-red-500 | border-inline-color: var(--color-red-500); |
| border-x-red-600 | border-inline-color: var(--color-red-600); |
| border-x-red-700 | border-inline-color: var(--color-red-700); |
| border-x-red-800 | border-inline-color: var(--color-red-800); |
| border-x-red-900 | border-inline-color: var(--color-red-900); |
| border-x-red-950 | border-inline-color: var(--color-red-950); |
| border-x-orange-50 | border-inline-color: var(--color-orange-50); |
| border-x-orange-100 | border-inline-color: var(--color-orange-100); |
| border-x-orange-200 | border-inline-color: var(--color-orange-200); |
| border-x-orange-300 | border-inline-color: var(--color-orange-300); |
| border-x-orange-400 | border-inline-color: var(--color-orange-400); |
| border-x-orange-500 | border-inline-color: var(--color-orange-500); |
| border-x-orange-600 | border-inline-color: var(--color-orange-600); |
| border-x-orange-700 | border-inline-color: var(--color-orange-700); |
| border-x-orange-800 | border-inline-color: var(--color-orange-800); |
| border-x-orange-900 | border-inline-color: var(--color-orange-900); |
| border-x-orange-950 | border-inline-color: var(--color-orange-950); |
| border-x-amber-50 | border-inline-color: var(--color-amber-50); |
| border-x-amber-100 | border-inline-color: var(--color-amber-100); |
| border-x-amber-200 | border-inline-color: var(--color-amber-200); |
| border-x-amber-300 | border-inline-color: var(--color-amber-300); |
| border-x-amber-400 | border-inline-color: var(--color-amber-400); |
| border-x-amber-500 | border-inline-color: var(--color-amber-500); |
| border-x-amber-600 | border-inline-color: var(--color-amber-600); |
| border-x-amber-700 | border-inline-color: var(--color-amber-700); |
| border-x-amber-800 | border-inline-color: var(--color-amber-800); |
| border-x-amber-900 | border-inline-color: var(--color-amber-900); |
| border-x-amber-950 | border-inline-color: var(--color-amber-950); |
| border-x-yellow-50 | border-inline-color: var(--color-yellow-50); |
| border-x-yellow-100 | border-inline-color: var(--color-yellow-100); |
| border-x-yellow-200 | border-inline-color: var(--color-yellow-200); |
| border-x-yellow-300 | border-inline-color: var(--color-yellow-300); |
| border-x-yellow-400 | border-inline-color: var(--color-yellow-400); |
| border-x-yellow-500 | border-inline-color: var(--color-yellow-500); |
| border-x-yellow-600 | border-inline-color: var(--color-yellow-600); |
| border-x-yellow-700 | border-inline-color: var(--color-yellow-700); |
| border-x-yellow-800 | border-inline-color: var(--color-yellow-800); |
| border-x-yellow-900 | border-inline-color: var(--color-yellow-900); |
| border-x-yellow-950 | border-inline-color: var(--color-yellow-950); |
| border-x-lime-50 | border-inline-color: var(--color-lime-50); |
| border-x-lime-100 | border-inline-color: var(--color-lime-100); |
| border-x-lime-200 | border-inline-color: var(--color-lime-200); |
| border-x-lime-300 | border-inline-color: var(--color-lime-300); |
| border-x-lime-400 | border-inline-color: var(--color-lime-400); |
| border-x-lime-500 | border-inline-color: var(--color-lime-500); |
| border-x-lime-600 | border-inline-color: var(--color-lime-600); |
| border-x-lime-700 | border-inline-color: var(--color-lime-700); |
| border-x-lime-800 | border-inline-color: var(--color-lime-800); |
| border-x-lime-900 | border-inline-color: var(--color-lime-900); |
| border-x-lime-950 | border-inline-color: var(--color-lime-950); |
| border-x-green-50 | border-inline-color: var(--color-green-50); |
| border-x-green-100 | border-inline-color: var(--color-green-100); |
| border-x-green-200 | border-inline-color: var(--color-green-200); |
| border-x-green-300 | border-inline-color: var(--color-green-300); |
| border-x-green-400 | border-inline-color: var(--color-green-400); |
| border-x-green-500 | border-inline-color: var(--color-green-500); |
| border-x-green-600 | border-inline-color: var(--color-green-600); |
| border-x-green-700 | border-inline-color: var(--color-green-700); |
| border-x-green-800 | border-inline-color: var(--color-green-800); |
| border-x-green-900 | border-inline-color: var(--color-green-900); |
| border-x-green-950 | border-inline-color: var(--color-green-950); |
| border-x-emerald-50 | border-inline-color: var(--color-emerald-50); |
| border-x-emerald-100 | border-inline-color: var(--color-emerald-100); |
| border-x-emerald-200 | border-inline-color: var(--color-emerald-200); |
| border-x-emerald-300 | border-inline-color: var(--color-emerald-300); |
| border-x-emerald-400 | border-inline-color: var(--color-emerald-400); |
| border-x-emerald-500 | border-inline-color: var(--color-emerald-500); |
| border-x-emerald-600 | border-inline-color: var(--color-emerald-600); |
| border-x-emerald-700 | border-inline-color: var(--color-emerald-700); |
| border-x-emerald-800 | border-inline-color: var(--color-emerald-800); |
| border-x-emerald-900 | border-inline-color: var(--color-emerald-900); |
| border-x-emerald-950 | border-inline-color: var(--color-emerald-950); |
| border-x-teal-50 | border-inline-color: var(--color-teal-50); |
| border-x-teal-100 | border-inline-color: var(--color-teal-100); |
| border-x-teal-200 | border-inline-color: var(--color-teal-200); |
| border-x-teal-300 | border-inline-color: var(--color-teal-300); |
| border-x-teal-400 | border-inline-color: var(--color-teal-400); |
| border-x-teal-500 | border-inline-color: var(--color-teal-500); |
| border-x-teal-600 | border-inline-color: var(--color-teal-600); |
| border-x-teal-700 | border-inline-color: var(--color-teal-700); |
| border-x-teal-800 | border-inline-color: var(--color-teal-800); |
| border-x-teal-900 | border-inline-color: var(--color-teal-900); |
| border-x-teal-950 | border-inline-color: var(--color-teal-950); |
| border-x-cyan-50 | border-inline-color: var(--color-cyan-50); |
| border-x-cyan-100 | border-inline-color: var(--color-cyan-100); |
| border-x-cyan-200 | border-inline-color: var(--color-cyan-200); |
| border-x-cyan-300 | border-inline-color: var(--color-cyan-300); |
| border-x-cyan-400 | border-inline-color: var(--color-cyan-400); |
| border-x-cyan-500 | border-inline-color: var(--color-cyan-500); |
| border-x-cyan-600 | border-inline-color: var(--color-cyan-600); |
| border-x-cyan-700 | border-inline-color: var(--color-cyan-700); |
| border-x-cyan-800 | border-inline-color: var(--color-cyan-800); |
| border-x-cyan-900 | border-inline-color: var(--color-cyan-900); |
| border-x-cyan-950 | border-inline-color: var(--color-cyan-950); |
| border-x-sky-50 | border-inline-color: var(--color-sky-50); |
| border-x-sky-100 | border-inline-color: var(--color-sky-100); |
| border-x-sky-200 | border-inline-color: var(--color-sky-200); |
| border-x-sky-300 | border-inline-color: var(--color-sky-300); |
| border-x-sky-400 | border-inline-color: var(--color-sky-400); |
| border-x-sky-500 | border-inline-color: var(--color-sky-500); |
| border-x-sky-600 | border-inline-color: var(--color-sky-600); |
| border-x-sky-700 | border-inline-color: var(--color-sky-700); |
| border-x-sky-800 | border-inline-color: var(--color-sky-800); |
| border-x-sky-900 | border-inline-color: var(--color-sky-900); |
| border-x-sky-950 | border-inline-color: var(--color-sky-950); |
| border-x-blue-50 | border-inline-color: var(--color-blue-50); |
| border-x-blue-100 | border-inline-color: var(--color-blue-100); |
| border-x-blue-200 | border-inline-color: var(--color-blue-200); |
| border-x-blue-300 | border-inline-color: var(--color-blue-300); |
| border-x-blue-400 | border-inline-color: var(--color-blue-400); |
| border-x-blue-500 | border-inline-color: var(--color-blue-500); |
| border-x-blue-600 | border-inline-color: var(--color-blue-600); |
| border-x-blue-700 | border-inline-color: var(--color-blue-700); |
| border-x-blue-800 | border-inline-color: var(--color-blue-800); |
| border-x-blue-900 | border-inline-color: var(--color-blue-900); |
| border-x-blue-950 | border-inline-color: var(--color-blue-950); |
| border-x-indigo-50 | border-inline-color: var(--color-indigo-50); |
| border-x-indigo-100 | border-inline-color: var(--color-indigo-100); |
| border-x-indigo-200 | border-inline-color: var(--color-indigo-200); |
| border-x-indigo-300 | border-inline-color: var(--color-indigo-300); |
| border-x-indigo-400 | border-inline-color: var(--color-indigo-400); |
| border-x-indigo-500 | border-inline-color: var(--color-indigo-500); |
| border-x-indigo-600 | border-inline-color: var(--color-indigo-600); |
| border-x-indigo-700 | border-inline-color: var(--color-indigo-700); |
| border-x-indigo-800 | border-inline-color: var(--color-indigo-800); |
| border-x-indigo-900 | border-inline-color: var(--color-indigo-900); |
| border-x-indigo-950 | border-inline-color: var(--color-indigo-950); |
| border-x-violet-50 | border-inline-color: var(--color-violet-50); |
| border-x-violet-100 | border-inline-color: var(--color-violet-100); |
| border-x-violet-200 | border-inline-color: var(--color-violet-200); |
| border-x-violet-300 | border-inline-color: var(--color-violet-300); |
| border-x-violet-400 | border-inline-color: var(--color-violet-400); |
| border-x-violet-500 | border-inline-color: var(--color-violet-500); |
| border-x-violet-600 | border-inline-color: var(--color-violet-600); |
| border-x-violet-700 | border-inline-color: var(--color-violet-700); |
| border-x-violet-800 | border-inline-color: var(--color-violet-800); |
| border-x-violet-900 | border-inline-color: var(--color-violet-900); |
| border-x-violet-950 | border-inline-color: var(--color-violet-950); |
| border-x-purple-50 | border-inline-color: var(--color-purple-50); |
| border-x-purple-100 | border-inline-color: var(--color-purple-100); |
| border-x-purple-200 | border-inline-color: var(--color-purple-200); |
| border-x-purple-300 | border-inline-color: var(--color-purple-300); |
| border-x-purple-400 | border-inline-color: var(--color-purple-400); |
| border-x-purple-500 | border-inline-color: var(--color-purple-500); |
| border-x-purple-600 | border-inline-color: var(--color-purple-600); |
| border-x-purple-700 | border-inline-color: var(--color-purple-700); |
| border-x-purple-800 | border-inline-color: var(--color-purple-800); |
| border-x-purple-900 | border-inline-color: var(--color-purple-900); |
| border-x-purple-950 | border-inline-color: var(--color-purple-950); |
| border-x-fuchsia-50 | border-inline-color: var(--color-fuchsia-50); |
| border-x-fuchsia-100 | border-inline-color: var(--color-fuchsia-100); |
| border-x-fuchsia-200 | border-inline-color: var(--color-fuchsia-200); |
| border-x-fuchsia-300 | border-inline-color: var(--color-fuchsia-300); |
| border-x-fuchsia-400 | border-inline-color: var(--color-fuchsia-400); |
| border-x-fuchsia-500 | border-inline-color: var(--color-fuchsia-500); |
| border-x-fuchsia-600 | border-inline-color: var(--color-fuchsia-600); |
| border-x-fuchsia-700 | border-inline-color: var(--color-fuchsia-700); |
| border-x-fuchsia-800 | border-inline-color: var(--color-fuchsia-800); |
| border-x-fuchsia-900 | border-inline-color: var(--color-fuchsia-900); |
| border-x-fuchsia-950 | border-inline-color: var(--color-fuchsia-950); |
| border-x-pink-50 | border-inline-color: var(--color-pink-50); |
| border-x-pink-100 | border-inline-color: var(--color-pink-100); |
| border-x-pink-200 | border-inline-color: var(--color-pink-200); |
| border-x-pink-300 | border-inline-color: var(--color-pink-300); |
| border-x-pink-400 | border-inline-color: var(--color-pink-400); |
| border-x-pink-500 | border-inline-color: var(--color-pink-500); |
| border-x-pink-600 | border-inline-color: var(--color-pink-600); |
| border-x-pink-700 | border-inline-color: var(--color-pink-700); |
| border-x-pink-800 | border-inline-color: var(--color-pink-800); |
| border-x-pink-900 | border-inline-color: var(--color-pink-900); |
| border-x-pink-950 | border-inline-color: var(--color-pink-950); |
| border-x-rose-50 | border-inline-color: var(--color-rose-50); |
| border-x-rose-100 | border-inline-color: var(--color-rose-100); |
| border-x-rose-200 | border-inline-color: var(--color-rose-200); |
| border-x-rose-300 | border-inline-color: var(--color-rose-300); |
| border-x-rose-400 | border-inline-color: var(--color-rose-400); |
| border-x-rose-500 | border-inline-color: var(--color-rose-500); |
| border-x-rose-600 | border-inline-color: var(--color-rose-600); |
| border-x-rose-700 | border-inline-color: var(--color-rose-700); |
| border-x-rose-800 | border-inline-color: var(--color-rose-800); |
| border-x-rose-900 | border-inline-color: var(--color-rose-900); |
| border-x-rose-950 | border-inline-color: var(--color-rose-950); |
| border-x-slate-50 | border-inline-color: var(--color-slate-50); |
| border-x-slate-100 | border-inline-color: var(--color-slate-100); |
| border-x-slate-200 | border-inline-color: var(--color-slate-200); |
| border-x-slate-300 | border-inline-color: var(--color-slate-300); |
| border-x-slate-400 | border-inline-color: var(--color-slate-400); |
| border-x-slate-500 | border-inline-color: var(--color-slate-500); |
| border-x-slate-600 | border-inline-color: var(--color-slate-600); |
| border-x-slate-700 | border-inline-color: var(--color-slate-700); |
| border-x-slate-800 | border-inline-color: var(--color-slate-800); |
| border-x-slate-900 | border-inline-color: var(--color-slate-900); |
| border-x-slate-950 | border-inline-color: var(--color-slate-950); |
| border-x-gray-50 | border-inline-color: var(--color-gray-50); |
| border-x-gray-100 | border-inline-color: var(--color-gray-100); |
| border-x-gray-200 | border-inline-color: var(--color-gray-200); |
| border-x-gray-300 | border-inline-color: var(--color-gray-300); |
| border-x-gray-400 | border-inline-color: var(--color-gray-400); |
| border-x-gray-500 | border-inline-color: var(--color-gray-500); |
| border-x-gray-600 | border-inline-color: var(--color-gray-600); |
| border-x-gray-700 | border-inline-color: var(--color-gray-700); |
| border-x-gray-800 | border-inline-color: var(--color-gray-800); |
| border-x-gray-900 | border-inline-color: var(--color-gray-900); |
| border-x-gray-950 | border-inline-color: var(--color-gray-950); |
| border-x-zinc-50 | border-inline-color: var(--color-zinc-50); |
| border-x-zinc-100 | border-inline-color: var(--color-zinc-100); |
| border-x-zinc-200 | border-inline-color: var(--color-zinc-200); |
| border-x-zinc-300 | border-inline-color: var(--color-zinc-300); |
| border-x-zinc-400 | border-inline-color: var(--color-zinc-400); |
| border-x-zinc-500 | border-inline-color: var(--color-zinc-500); |
| border-x-zinc-600 | border-inline-color: var(--color-zinc-600); |
| border-x-zinc-700 | border-inline-color: var(--color-zinc-700); |
| border-x-zinc-800 | border-inline-color: var(--color-zinc-800); |
| border-x-zinc-900 | border-inline-color: var(--color-zinc-900); |
| border-x-zinc-950 | border-inline-color: var(--color-zinc-950); |
| border-x-neutral-50 | border-inline-color: var(--color-neutral-50); |
| border-x-neutral-100 | border-inline-color: var(--color-neutral-100); |
| border-x-neutral-200 | border-inline-color: var(--color-neutral-200); |
| border-x-neutral-300 | border-inline-color: var(--color-neutral-300); |
| border-x-neutral-400 | border-inline-color: var(--color-neutral-400); |
| border-x-neutral-500 | border-inline-color: var(--color-neutral-500); |
| border-x-neutral-600 | border-inline-color: var(--color-neutral-600); |
| border-x-neutral-700 | border-inline-color: var(--color-neutral-700); |
| border-x-neutral-800 | border-inline-color: var(--color-neutral-800); |
| border-x-neutral-900 | border-inline-color: var(--color-neutral-900); |
| border-x-neutral-950 | border-inline-color: var(--color-neutral-950); |
| border-x-stone-50 | border-inline-color: var(--color-stone-50); |
| border-x-stone-100 | border-inline-color: var(--color-stone-100); |
| border-x-stone-200 | border-inline-color: var(--color-stone-200); |
| border-x-stone-300 | border-inline-color: var(--color-stone-300); |
| border-x-stone-400 | border-inline-color: var(--color-stone-400); |
| border-x-stone-500 | border-inline-color: var(--color-stone-500); |
| border-x-stone-600 | border-inline-color: var(--color-stone-600); |
| border-x-stone-700 | border-inline-color: var(--color-stone-700); |
| border-x-stone-800 | border-inline-color: var(--color-stone-800); |
| border-x-stone-900 | border-inline-color: var(--color-stone-900); |
| border-x-stone-950 | border-inline-color: var(--color-stone-950); |
| border-x-(<custom-property>) | border-inline-color: var(<custom-property>); |
| border-x-[<value>] | border-inline-color: <value>; |
| border-y-inherit | border-block-color: inherit; |
| border-y-current | border-block-color: currentColor; |
| border-y-transparent | border-block-color: transparent; |
| border-y-black | border-block-color: var(--color-black); /* #000 */ |
| border-y-white | border-block-color: var(--color-white); /* #fff */ |
| border-y-red-50 | border-block-color: var(--color-red-50); |
| border-y-red-100 | border-block-color: var(--color-red-100); |
| border-y-red-200 | border-block-color: var(--color-red-200); |
| border-y-red-300 | border-block-color: var(--color-red-300); |
| border-y-red-400 | border-block-color: var(--color-red-400); |
| border-y-red-500 | border-block-color: var(--color-red-500); |
| border-y-red-600 | border-block-color: var(--color-red-600); |
| border-y-red-700 | border-block-color: var(--color-red-700); |
| border-y-red-800 | border-block-color: var(--color-red-800); |
| border-y-red-900 | border-block-color: var(--color-red-900); |
| border-y-red-950 | border-block-color: var(--color-red-950); |
| border-y-orange-50 | border-block-color: var(--color-orange-50); |
| border-y-orange-100 | border-block-color: var(--color-orange-100); |
| border-y-orange-200 | border-block-color: var(--color-orange-200); |
| border-y-orange-300 | border-block-color: var(--color-orange-300); |
| border-y-orange-400 | border-block-color: var(--color-orange-400); |
| border-y-orange-500 | border-block-color: var(--color-orange-500); |
| border-y-orange-600 | border-block-color: var(--color-orange-600); |
| border-y-orange-700 | border-block-color: var(--color-orange-700); |
| border-y-orange-800 | border-block-color: var(--color-orange-800); |
| border-y-orange-900 | border-block-color: var(--color-orange-900); |
| border-y-orange-950 | border-block-color: var(--color-orange-950); |
| border-y-amber-50 | border-block-color: var(--color-amber-50); |
| border-y-amber-100 | border-block-color: var(--color-amber-100); |
| border-y-amber-200 | border-block-color: var(--color-amber-200); |
| border-y-amber-300 | border-block-color: var(--color-amber-300); |
| border-y-amber-400 | border-block-color: var(--color-amber-400); |
| border-y-amber-500 | border-block-color: var(--color-amber-500); |
| border-y-amber-600 | border-block-color: var(--color-amber-600); |
| border-y-amber-700 | border-block-color: var(--color-amber-700); |
| border-y-amber-800 | border-block-color: var(--color-amber-800); |
| border-y-amber-900 | border-block-color: var(--color-amber-900); |
| border-y-amber-950 | border-block-color: var(--color-amber-950); |
| border-y-yellow-50 | border-block-color: var(--color-yellow-50); |
| border-y-yellow-100 | border-block-color: var(--color-yellow-100); |
| border-y-yellow-200 | border-block-color: var(--color-yellow-200); |
| border-y-yellow-300 | border-block-color: var(--color-yellow-300); |
| border-y-yellow-400 | border-block-color: var(--color-yellow-400); |
| border-y-yellow-500 | border-block-color: var(--color-yellow-500); |
| border-y-yellow-600 | border-block-color: var(--color-yellow-600); |
| border-y-yellow-700 | border-block-color: var(--color-yellow-700); |
| border-y-yellow-800 | border-block-color: var(--color-yellow-800); |
| border-y-yellow-900 | border-block-color: var(--color-yellow-900); |
| border-y-yellow-950 | border-block-color: var(--color-yellow-950); |
| border-y-lime-50 | border-block-color: var(--color-lime-50); |
| border-y-lime-100 | border-block-color: var(--color-lime-100); |
| border-y-lime-200 | border-block-color: var(--color-lime-200); |
| border-y-lime-300 | border-block-color: var(--color-lime-300); |
| border-y-lime-400 | border-block-color: var(--color-lime-400); |
| border-y-lime-500 | border-block-color: var(--color-lime-500); |
| border-y-lime-600 | border-block-color: var(--color-lime-600); |
| border-y-lime-700 | border-block-color: var(--color-lime-700); |
| border-y-lime-800 | border-block-color: var(--color-lime-800); |
| border-y-lime-900 | border-block-color: var(--color-lime-900); |
| border-y-lime-950 | border-block-color: var(--color-lime-950); |
| border-y-green-50 | border-block-color: var(--color-green-50); |
| border-y-green-100 | border-block-color: var(--color-green-100); |
| border-y-green-200 | border-block-color: var(--color-green-200); |
| border-y-green-300 | border-block-color: var(--color-green-300); |
| border-y-green-400 | border-block-color: var(--color-green-400); |
| border-y-green-500 | border-block-color: var(--color-green-500); |
| border-y-green-600 | border-block-color: var(--color-green-600); |
| border-y-green-700 | border-block-color: var(--color-green-700); |
| border-y-green-800 | border-block-color: var(--color-green-800); |
| border-y-green-900 | border-block-color: var(--color-green-900); |
| border-y-green-950 | border-block-color: var(--color-green-950); |
| border-y-emerald-50 | border-block-color: var(--color-emerald-50); |
| border-y-emerald-100 | border-block-color: var(--color-emerald-100); |
| border-y-emerald-200 | border-block-color: var(--color-emerald-200); |
| border-y-emerald-300 | border-block-color: var(--color-emerald-300); |
| border-y-emerald-400 | border-block-color: var(--color-emerald-400); |
| border-y-emerald-500 | border-block-color: var(--color-emerald-500); |
| border-y-emerald-600 | border-block-color: var(--color-emerald-600); |
| border-y-emerald-700 | border-block-color: var(--color-emerald-700); |
| border-y-emerald-800 | border-block-color: var(--color-emerald-800); |
| border-y-emerald-900 | border-block-color: var(--color-emerald-900); |
| border-y-emerald-950 | border-block-color: var(--color-emerald-950); |
| border-y-teal-50 | border-block-color: var(--color-teal-50); |
| border-y-teal-100 | border-block-color: var(--color-teal-100); |
| border-y-teal-200 | border-block-color: var(--color-teal-200); |
| border-y-teal-300 | border-block-color: var(--color-teal-300); |
| border-y-teal-400 | border-block-color: var(--color-teal-400); |
| border-y-teal-500 | border-block-color: var(--color-teal-500); |
| border-y-teal-600 | border-block-color: var(--color-teal-600); |
| border-y-teal-700 | border-block-color: var(--color-teal-700); |
| border-y-teal-800 | border-block-color: var(--color-teal-800); |
| border-y-teal-900 | border-block-color: var(--color-teal-900); |
| border-y-teal-950 | border-block-color: var(--color-teal-950); |
| border-y-cyan-50 | border-block-color: var(--color-cyan-50); |
| border-y-cyan-100 | border-block-color: var(--color-cyan-100); |
| border-y-cyan-200 | border-block-color: var(--color-cyan-200); |
| border-y-cyan-300 | border-block-color: var(--color-cyan-300); |
| border-y-cyan-400 | border-block-color: var(--color-cyan-400); |
| border-y-cyan-500 | border-block-color: var(--color-cyan-500); |
| border-y-cyan-600 | border-block-color: var(--color-cyan-600); |
| border-y-cyan-700 | border-block-color: var(--color-cyan-700); |
| border-y-cyan-800 | border-block-color: var(--color-cyan-800); |
| border-y-cyan-900 | border-block-color: var(--color-cyan-900); |
| border-y-cyan-950 | border-block-color: var(--color-cyan-950); |
| border-y-sky-50 | border-block-color: var(--color-sky-50); |
| border-y-sky-100 | border-block-color: var(--color-sky-100); |
| border-y-sky-200 | border-block-color: var(--color-sky-200); |
| border-y-sky-300 | border-block-color: var(--color-sky-300); |
| border-y-sky-400 | border-block-color: var(--color-sky-400); |
| border-y-sky-500 | border-block-color: var(--color-sky-500); |
| border-y-sky-600 | border-block-color: var(--color-sky-600); |
| border-y-sky-700 | border-block-color: var(--color-sky-700); |
| border-y-sky-800 | border-block-color: var(--color-sky-800); |
| border-y-sky-900 | border-block-color: var(--color-sky-900); |
| border-y-sky-950 | border-block-color: var(--color-sky-950); |
| border-y-blue-50 | border-block-color: var(--color-blue-50); |
| border-y-blue-100 | border-block-color: var(--color-blue-100); |
| border-y-blue-200 | border-block-color: var(--color-blue-200); |
| border-y-blue-300 | border-block-color: var(--color-blue-300); |
| border-y-blue-400 | border-block-color: var(--color-blue-400); |
| border-y-blue-500 | border-block-color: var(--color-blue-500); |
| border-y-blue-600 | border-block-color: var(--color-blue-600); |
| border-y-blue-700 | border-block-color: var(--color-blue-700); |
| border-y-blue-800 | border-block-color: var(--color-blue-800); |
| border-y-blue-900 | border-block-color: var(--color-blue-900); |
| border-y-blue-950 | border-block-color: var(--color-blue-950); |
| border-y-indigo-50 | border-block-color: var(--color-indigo-50); |
| border-y-indigo-100 | border-block-color: var(--color-indigo-100); |
| border-y-indigo-200 | border-block-color: var(--color-indigo-200); |
| border-y-indigo-300 | border-block-color: var(--color-indigo-300); |
| border-y-indigo-400 | border-block-color: var(--color-indigo-400); |
| border-y-indigo-500 | border-block-color: var(--color-indigo-500); |
| border-y-indigo-600 | border-block-color: var(--color-indigo-600); |
| border-y-indigo-700 | border-block-color: var(--color-indigo-700); |
| border-y-indigo-800 | border-block-color: var(--color-indigo-800); |
| border-y-indigo-900 | border-block-color: var(--color-indigo-900); |
| border-y-indigo-950 | border-block-color: var(--color-indigo-950); |
| border-y-violet-50 | border-block-color: var(--color-violet-50); |
| border-y-violet-100 | border-block-color: var(--color-violet-100); |
| border-y-violet-200 | border-block-color: var(--color-violet-200); |
| border-y-violet-300 | border-block-color: var(--color-violet-300); |
| border-y-violet-400 | border-block-color: var(--color-violet-400); |
| border-y-violet-500 | border-block-color: var(--color-violet-500); |
| border-y-violet-600 | border-block-color: var(--color-violet-600); |
| border-y-violet-700 | border-block-color: var(--color-violet-700); |
| border-y-violet-800 | border-block-color: var(--color-violet-800); |
| border-y-violet-900 | border-block-color: var(--color-violet-900); |
| border-y-violet-950 | border-block-color: var(--color-violet-950); |
| border-y-purple-50 | border-block-color: var(--color-purple-50); |
| border-y-purple-100 | border-block-color: var(--color-purple-100); |
| border-y-purple-200 | border-block-color: var(--color-purple-200); |
| border-y-purple-300 | border-block-color: var(--color-purple-300); |
| border-y-purple-400 | border-block-color: var(--color-purple-400); |
| border-y-purple-500 | border-block-color: var(--color-purple-500); |
| border-y-purple-600 | border-block-color: var(--color-purple-600); |
| border-y-purple-700 | border-block-color: var(--color-purple-700); |
| border-y-purple-800 | border-block-color: var(--color-purple-800); |
| border-y-purple-900 | border-block-color: var(--color-purple-900); |
| border-y-purple-950 | border-block-color: var(--color-purple-950); |
| border-y-fuchsia-50 | border-block-color: var(--color-fuchsia-50); |
| border-y-fuchsia-100 | border-block-color: var(--color-fuchsia-100); |
| border-y-fuchsia-200 | border-block-color: var(--color-fuchsia-200); |
| border-y-fuchsia-300 | border-block-color: var(--color-fuchsia-300); |
| border-y-fuchsia-400 | border-block-color: var(--color-fuchsia-400); |
| border-y-fuchsia-500 | border-block-color: var(--color-fuchsia-500); |
| border-y-fuchsia-600 | border-block-color: var(--color-fuchsia-600); |
| border-y-fuchsia-700 | border-block-color: var(--color-fuchsia-700); |
| border-y-fuchsia-800 | border-block-color: var(--color-fuchsia-800); |
| border-y-fuchsia-900 | border-block-color: var(--color-fuchsia-900); |
| border-y-fuchsia-950 | border-block-color: var(--color-fuchsia-950); |
| border-y-pink-50 | border-block-color: var(--color-pink-50); |
| border-y-pink-100 | border-block-color: var(--color-pink-100); |
| border-y-pink-200 | border-block-color: var(--color-pink-200); |
| border-y-pink-300 | border-block-color: var(--color-pink-300); |
| border-y-pink-400 | border-block-color: var(--color-pink-400); |
| border-y-pink-500 | border-block-color: var(--color-pink-500); |
| border-y-pink-600 | border-block-color: var(--color-pink-600); |
| border-y-pink-700 | border-block-color: var(--color-pink-700); |
| border-y-pink-800 | border-block-color: var(--color-pink-800); |
| border-y-pink-900 | border-block-color: var(--color-pink-900); |
| border-y-pink-950 | border-block-color: var(--color-pink-950); |
| border-y-rose-50 | border-block-color: var(--color-rose-50); |
| border-y-rose-100 | border-block-color: var(--color-rose-100); |
| border-y-rose-200 | border-block-color: var(--color-rose-200); |
| border-y-rose-300 | border-block-color: var(--color-rose-300); |
| border-y-rose-400 | border-block-color: var(--color-rose-400); |
| border-y-rose-500 | border-block-color: var(--color-rose-500); |
| border-y-rose-600 | border-block-color: var(--color-rose-600); |
| border-y-rose-700 | border-block-color: var(--color-rose-700); |
| border-y-rose-800 | border-block-color: var(--color-rose-800); |
| border-y-rose-900 | border-block-color: var(--color-rose-900); |
| border-y-rose-950 | border-block-color: var(--color-rose-950); |
| border-y-slate-50 | border-block-color: var(--color-slate-50); |
| border-y-slate-100 | border-block-color: var(--color-slate-100); |
| border-y-slate-200 | border-block-color: var(--color-slate-200); |
| border-y-slate-300 | border-block-color: var(--color-slate-300); |
| border-y-slate-400 | border-block-color: var(--color-slate-400); |
| border-y-slate-500 | border-block-color: var(--color-slate-500); |
| border-y-slate-600 | border-block-color: var(--color-slate-600); |
| border-y-slate-700 | border-block-color: var(--color-slate-700); |
| border-y-slate-800 | border-block-color: var(--color-slate-800); |
| border-y-slate-900 | border-block-color: var(--color-slate-900); |
| border-y-slate-950 | border-block-color: var(--color-slate-950); |
| border-y-gray-50 | border-block-color: var(--color-gray-50); |
| border-y-gray-100 | border-block-color: var(--color-gray-100); |
| border-y-gray-200 | border-block-color: var(--color-gray-200); |
| border-y-gray-300 | border-block-color: var(--color-gray-300); |
| border-y-gray-400 | border-block-color: var(--color-gray-400); |
| border-y-gray-500 | border-block-color: var(--color-gray-500); |
| border-y-gray-600 | border-block-color: var(--color-gray-600); |
| border-y-gray-700 | border-block-color: var(--color-gray-700); |
| border-y-gray-800 | border-block-color: var(--color-gray-800); |
| border-y-gray-900 | border-block-color: var(--color-gray-900); |
| border-y-gray-950 | border-block-color: var(--color-gray-950); |
| border-y-zinc-50 | border-block-color: var(--color-zinc-50); |
| border-y-zinc-100 | border-block-color: var(--color-zinc-100); |
| border-y-zinc-200 | border-block-color: var(--color-zinc-200); |
| border-y-zinc-300 | border-block-color: var(--color-zinc-300); |
| border-y-zinc-400 | border-block-color: var(--color-zinc-400); |
| border-y-zinc-500 | border-block-color: var(--color-zinc-500); |
| border-y-zinc-600 | border-block-color: var(--color-zinc-600); |
| border-y-zinc-700 | border-block-color: var(--color-zinc-700); |
| border-y-zinc-800 | border-block-color: var(--color-zinc-800); |
| border-y-zinc-900 | border-block-color: var(--color-zinc-900); |
| border-y-zinc-950 | border-block-color: var(--color-zinc-950); |
| border-y-neutral-50 | border-block-color: var(--color-neutral-50); |
| border-y-neutral-100 | border-block-color: var(--color-neutral-100); |
| border-y-neutral-200 | border-block-color: var(--color-neutral-200); |
| border-y-neutral-300 | border-block-color: var(--color-neutral-300); |
| border-y-neutral-400 | border-block-color: var(--color-neutral-400); |
| border-y-neutral-500 | border-block-color: var(--color-neutral-500); |
| border-y-neutral-600 | border-block-color: var(--color-neutral-600); |
| border-y-neutral-700 | border-block-color: var(--color-neutral-700); |
| border-y-neutral-800 | border-block-color: var(--color-neutral-800); |
| border-y-neutral-900 | border-block-color: var(--color-neutral-900); |
| border-y-neutral-950 | border-block-color: var(--color-neutral-950); |
| border-y-stone-50 | border-block-color: var(--color-stone-50); |
| border-y-stone-100 | border-block-color: var(--color-stone-100); |
| border-y-stone-200 | border-block-color: var(--color-stone-200); |
| border-y-stone-300 | border-block-color: var(--color-stone-300); |
| border-y-stone-400 | border-block-color: var(--color-stone-400); |
| border-y-stone-500 | border-block-color: var(--color-stone-500); |
| border-y-stone-600 | border-block-color: var(--color-stone-600); |
| border-y-stone-700 | border-block-color: var(--color-stone-700); |
| border-y-stone-800 | border-block-color: var(--color-stone-800); |
| border-y-stone-900 | border-block-color: var(--color-stone-900); |
| border-y-stone-950 | border-block-color: var(--color-stone-950); |
| border-y-(<custom-property>) | border-block-color: var(<custom-property>); |
| border-y-[<value>] | border-block-color: <value>; |
| border-s-inherit | border-inline-start-color: inherit; |
| border-s-current | border-inline-start-color: currentColor; |
| border-s-transparent | border-inline-start-color: transparent; |
| border-s-black | border-inline-start-color: var(--color-black); /* #000 */ |
| border-s-white | border-inline-start-color: var(--color-white); /* #fff */ |
| border-s-red-50 | border-inline-start-color: var(--color-red-50); |
| border-s-red-100 | border-inline-start-color: var(--color-red-100); |
| border-s-red-200 | border-inline-start-color: var(--color-red-200); |
| border-s-red-300 | border-inline-start-color: var(--color-red-300); |
| border-s-red-400 | border-inline-start-color: var(--color-red-400); |
| border-s-red-500 | border-inline-start-color: var(--color-red-500); |
| border-s-red-600 | border-inline-start-color: var(--color-red-600); |
| border-s-red-700 | border-inline-start-color: var(--color-red-700); |
| border-s-red-800 | border-inline-start-color: var(--color-red-800); |
| border-s-red-900 | border-inline-start-color: var(--color-red-900); |
| border-s-red-950 | border-inline-start-color: var(--color-red-950); |
| border-s-orange-50 | border-inline-start-color: var(--color-orange-50); |
| border-s-orange-100 | border-inline-start-color: var(--color-orange-100); |
| border-s-orange-200 | border-inline-start-color: var(--color-orange-200); |
| border-s-orange-300 | border-inline-start-color: var(--color-orange-300); |
| border-s-orange-400 | border-inline-start-color: var(--color-orange-400); |
| border-s-orange-500 | border-inline-start-color: var(--color-orange-500); |
| border-s-orange-600 | border-inline-start-color: var(--color-orange-600); |
| border-s-orange-700 | border-inline-start-color: var(--color-orange-700); |
| border-s-orange-800 | border-inline-start-color: var(--color-orange-800); |
| border-s-orange-900 | border-inline-start-color: var(--color-orange-900); |
| border-s-orange-950 | border-inline-start-color: var(--color-orange-950); |
| border-s-amber-50 | border-inline-start-color: var(--color-amber-50); |
| border-s-amber-100 | border-inline-start-color: var(--color-amber-100); |
| border-s-amber-200 | border-inline-start-color: var(--color-amber-200); |
| border-s-amber-300 | border-inline-start-color: var(--color-amber-300); |
| border-s-amber-400 | border-inline-start-color: var(--color-amber-400); |
| border-s-amber-500 | border-inline-start-color: var(--color-amber-500); |
| border-s-amber-600 | border-inline-start-color: var(--color-amber-600); |
| border-s-amber-700 | border-inline-start-color: var(--color-amber-700); |
| border-s-amber-800 | border-inline-start-color: var(--color-amber-800); |
| border-s-amber-900 | border-inline-start-color: var(--color-amber-900); |
| border-s-amber-950 | border-inline-start-color: var(--color-amber-950); |
| border-s-yellow-50 | border-inline-start-color: var(--color-yellow-50); |
| border-s-yellow-100 | border-inline-start-color: var(--color-yellow-100); |
| border-s-yellow-200 | border-inline-start-color: var(--color-yellow-200); |
| border-s-yellow-300 | border-inline-start-color: var(--color-yellow-300); |
| border-s-yellow-400 | border-inline-start-color: var(--color-yellow-400); |
| border-s-yellow-500 | border-inline-start-color: var(--color-yellow-500); |
| border-s-yellow-600 | border-inline-start-color: var(--color-yellow-600); |
| border-s-yellow-700 | border-inline-start-color: var(--color-yellow-700); |
| border-s-yellow-800 | border-inline-start-color: var(--color-yellow-800); |
| border-s-yellow-900 | border-inline-start-color: var(--color-yellow-900); |
| border-s-yellow-950 | border-inline-start-color: var(--color-yellow-950); |
| border-s-lime-50 | border-inline-start-color: var(--color-lime-50); |
| border-s-lime-100 | border-inline-start-color: var(--color-lime-100); |
| border-s-lime-200 | border-inline-start-color: var(--color-lime-200); |
| border-s-lime-300 | border-inline-start-color: var(--color-lime-300); |
| border-s-lime-400 | border-inline-start-color: var(--color-lime-400); |
| border-s-lime-500 | border-inline-start-color: var(--color-lime-500); |
| border-s-lime-600 | border-inline-start-color: var(--color-lime-600); |
| border-s-lime-700 | border-inline-start-color: var(--color-lime-700); |
| border-s-lime-800 | border-inline-start-color: var(--color-lime-800); |
| border-s-lime-900 | border-inline-start-color: var(--color-lime-900); |
| border-s-lime-950 | border-inline-start-color: var(--color-lime-950); |
| border-s-green-50 | border-inline-start-color: var(--color-green-50); |
| border-s-green-100 | border-inline-start-color: var(--color-green-100); |
| border-s-green-200 | border-inline-start-color: var(--color-green-200); |
| border-s-green-300 | border-inline-start-color: var(--color-green-300); |
| border-s-green-400 | border-inline-start-color: var(--color-green-400); |
| border-s-green-500 | border-inline-start-color: var(--color-green-500); |
| border-s-green-600 | border-inline-start-color: var(--color-green-600); |
| border-s-green-700 | border-inline-start-color: var(--color-green-700); |
| border-s-green-800 | border-inline-start-color: var(--color-green-800); |
| border-s-green-900 | border-inline-start-color: var(--color-green-900); |
| border-s-green-950 | border-inline-start-color: var(--color-green-950); |
| border-s-emerald-50 | border-inline-start-color: var(--color-emerald-50); |
| border-s-emerald-100 | border-inline-start-color: var(--color-emerald-100); |
| border-s-emerald-200 | border-inline-start-color: var(--color-emerald-200); |
| border-s-emerald-300 | border-inline-start-color: var(--color-emerald-300); |
| border-s-emerald-400 | border-inline-start-color: var(--color-emerald-400); |
| border-s-emerald-500 | border-inline-start-color: var(--color-emerald-500); |
| border-s-emerald-600 | border-inline-start-color: var(--color-emerald-600); |
| border-s-emerald-700 | border-inline-start-color: var(--color-emerald-700); |
| border-s-emerald-800 | border-inline-start-color: var(--color-emerald-800); |
| border-s-emerald-900 | border-inline-start-color: var(--color-emerald-900); |
| border-s-emerald-950 | border-inline-start-color: var(--color-emerald-950); |
| border-s-teal-50 | border-inline-start-color: var(--color-teal-50); |
| border-s-teal-100 | border-inline-start-color: var(--color-teal-100); |
| border-s-teal-200 | border-inline-start-color: var(--color-teal-200); |
| border-s-teal-300 | border-inline-start-color: var(--color-teal-300); |
| border-s-teal-400 | border-inline-start-color: var(--color-teal-400); |
| border-s-teal-500 | border-inline-start-color: var(--color-teal-500); |
| border-s-teal-600 | border-inline-start-color: var(--color-teal-600); |
| border-s-teal-700 | border-inline-start-color: var(--color-teal-700); |
| border-s-teal-800 | border-inline-start-color: var(--color-teal-800); |
| border-s-teal-900 | border-inline-start-color: var(--color-teal-900); |
| border-s-teal-950 | border-inline-start-color: var(--color-teal-950); |
| border-s-cyan-50 | border-inline-start-color: var(--color-cyan-50); |
| border-s-cyan-100 | border-inline-start-color: var(--color-cyan-100); |
| border-s-cyan-200 | border-inline-start-color: var(--color-cyan-200); |
| border-s-cyan-300 | border-inline-start-color: var(--color-cyan-300); |
| border-s-cyan-400 | border-inline-start-color: var(--color-cyan-400); |
| border-s-cyan-500 | border-inline-start-color: var(--color-cyan-500); |
| border-s-cyan-600 | border-inline-start-color: var(--color-cyan-600); |
| border-s-cyan-700 | border-inline-start-color: var(--color-cyan-700); |
| border-s-cyan-800 | border-inline-start-color: var(--color-cyan-800); |
| border-s-cyan-900 | border-inline-start-color: var(--color-cyan-900); |
| border-s-cyan-950 | border-inline-start-color: var(--color-cyan-950); |
| border-s-sky-50 | border-inline-start-color: var(--color-sky-50); |
| border-s-sky-100 | border-inline-start-color: var(--color-sky-100); |
| border-s-sky-200 | border-inline-start-color: var(--color-sky-200); |
| border-s-sky-300 | border-inline-start-color: var(--color-sky-300); |
| border-s-sky-400 | border-inline-start-color: var(--color-sky-400); |
| border-s-sky-500 | border-inline-start-color: var(--color-sky-500); |
| border-s-sky-600 | border-inline-start-color: var(--color-sky-600); |
| border-s-sky-700 | border-inline-start-color: var(--color-sky-700); |
| border-s-sky-800 | border-inline-start-color: var(--color-sky-800); |
| border-s-sky-900 | border-inline-start-color: var(--color-sky-900); |
| border-s-sky-950 | border-inline-start-color: var(--color-sky-950); |
| border-s-blue-50 | border-inline-start-color: var(--color-blue-50); |
| border-s-blue-100 | border-inline-start-color: var(--color-blue-100); |
| border-s-blue-200 | border-inline-start-color: var(--color-blue-200); |
| border-s-blue-300 | border-inline-start-color: var(--color-blue-300); |
| border-s-blue-400 | border-inline-start-color: var(--color-blue-400); |
| border-s-blue-500 | border-inline-start-color: var(--color-blue-500); |
| border-s-blue-600 | border-inline-start-color: var(--color-blue-600); |
| border-s-blue-700 | border-inline-start-color: var(--color-blue-700); |
| border-s-blue-800 | border-inline-start-color: var(--color-blue-800); |
| border-s-blue-900 | border-inline-start-color: var(--color-blue-900); |
| border-s-blue-950 | border-inline-start-color: var(--color-blue-950); |
| border-s-indigo-50 | border-inline-start-color: var(--color-indigo-50); |
| border-s-indigo-100 | border-inline-start-color: var(--color-indigo-100); |
| border-s-indigo-200 | border-inline-start-color: var(--color-indigo-200); |
| border-s-indigo-300 | border-inline-start-color: var(--color-indigo-300); |
| border-s-indigo-400 | border-inline-start-color: var(--color-indigo-400); |
| border-s-indigo-500 | border-inline-start-color: var(--color-indigo-500); |
| border-s-indigo-600 | border-inline-start-color: var(--color-indigo-600); |
| border-s-indigo-700 | border-inline-start-color: var(--color-indigo-700); |
| border-s-indigo-800 | border-inline-start-color: var(--color-indigo-800); |
| border-s-indigo-900 | border-inline-start-color: var(--color-indigo-900); |
| border-s-indigo-950 | border-inline-start-color: var(--color-indigo-950); |
| border-s-violet-50 | border-inline-start-color: var(--color-violet-50); |
| border-s-violet-100 | border-inline-start-color: var(--color-violet-100); |
| border-s-violet-200 | border-inline-start-color: var(--color-violet-200); |
| border-s-violet-300 | border-inline-start-color: var(--color-violet-300); |
| border-s-violet-400 | border-inline-start-color: var(--color-violet-400); |
| border-s-violet-500 | border-inline-start-color: var(--color-violet-500); |
| border-s-violet-600 | border-inline-start-color: var(--color-violet-600); |
| border-s-violet-700 | border-inline-start-color: var(--color-violet-700); |
| border-s-violet-800 | border-inline-start-color: var(--color-violet-800); |
| border-s-violet-900 | border-inline-start-color: var(--color-violet-900); |
| border-s-violet-950 | border-inline-start-color: var(--color-violet-950); |
| border-s-purple-50 | border-inline-start-color: var(--color-purple-50); |
| border-s-purple-100 | border-inline-start-color: var(--color-purple-100); |
| border-s-purple-200 | border-inline-start-color: var(--color-purple-200); |
| border-s-purple-300 | border-inline-start-color: var(--color-purple-300); |
| border-s-purple-400 | border-inline-start-color: var(--color-purple-400); |
| border-s-purple-500 | border-inline-start-color: var(--color-purple-500); |
| border-s-purple-600 | border-inline-start-color: var(--color-purple-600); |
| border-s-purple-700 | border-inline-start-color: var(--color-purple-700); |
| border-s-purple-800 | border-inline-start-color: var(--color-purple-800); |
| border-s-purple-900 | border-inline-start-color: var(--color-purple-900); |
| border-s-purple-950 | border-inline-start-color: var(--color-purple-950); |
| border-s-fuchsia-50 | border-inline-start-color: var(--color-fuchsia-50); |
| border-s-fuchsia-100 | border-inline-start-color: var(--color-fuchsia-100); |
| border-s-fuchsia-200 | border-inline-start-color: var(--color-fuchsia-200); |
| border-s-fuchsia-300 | border-inline-start-color: var(--color-fuchsia-300); |
| border-s-fuchsia-400 | border-inline-start-color: var(--color-fuchsia-400); |
| border-s-fuchsia-500 | border-inline-start-color: var(--color-fuchsia-500); |
| border-s-fuchsia-600 | border-inline-start-color: var(--color-fuchsia-600); |
| border-s-fuchsia-700 | border-inline-start-color: var(--color-fuchsia-700); |
| border-s-fuchsia-800 | border-inline-start-color: var(--color-fuchsia-800); |
| border-s-fuchsia-900 | border-inline-start-color: var(--color-fuchsia-900); |
| border-s-fuchsia-950 | border-inline-start-color: var(--color-fuchsia-950); |
| border-s-pink-50 | border-inline-start-color: var(--color-pink-50); |
| border-s-pink-100 | border-inline-start-color: var(--color-pink-100); |
| border-s-pink-200 | border-inline-start-color: var(--color-pink-200); |
| border-s-pink-300 | border-inline-start-color: var(--color-pink-300); |
| border-s-pink-400 | border-inline-start-color: var(--color-pink-400); |
| border-s-pink-500 | border-inline-start-color: var(--color-pink-500); |
| border-s-pink-600 | border-inline-start-color: var(--color-pink-600); |
| border-s-pink-700 | border-inline-start-color: var(--color-pink-700); |
| border-s-pink-800 | border-inline-start-color: var(--color-pink-800); |
| border-s-pink-900 | border-inline-start-color: var(--color-pink-900); |
| border-s-pink-950 | border-inline-start-color: var(--color-pink-950); |
| border-s-rose-50 | border-inline-start-color: var(--color-rose-50); |
| border-s-rose-100 | border-inline-start-color: var(--color-rose-100); |
| border-s-rose-200 | border-inline-start-color: var(--color-rose-200); |
| border-s-rose-300 | border-inline-start-color: var(--color-rose-300); |
| border-s-rose-400 | border-inline-start-color: var(--color-rose-400); |
| border-s-rose-500 | border-inline-start-color: var(--color-rose-500); |
| border-s-rose-600 | border-inline-start-color: var(--color-rose-600); |
| border-s-rose-700 | border-inline-start-color: var(--color-rose-700); |
| border-s-rose-800 | border-inline-start-color: var(--color-rose-800); |
| border-s-rose-900 | border-inline-start-color: var(--color-rose-900); |
| border-s-rose-950 | border-inline-start-color: var(--color-rose-950); |
| border-s-slate-50 | border-inline-start-color: var(--color-slate-50); |
| border-s-slate-100 | border-inline-start-color: var(--color-slate-100); |
| border-s-slate-200 | border-inline-start-color: var(--color-slate-200); |
| border-s-slate-300 | border-inline-start-color: var(--color-slate-300); |
| border-s-slate-400 | border-inline-start-color: var(--color-slate-400); |
| border-s-slate-500 | border-inline-start-color: var(--color-slate-500); |
| border-s-slate-600 | border-inline-start-color: var(--color-slate-600); |
| border-s-slate-700 | border-inline-start-color: var(--color-slate-700); |
| border-s-slate-800 | border-inline-start-color: var(--color-slate-800); |
| border-s-slate-900 | border-inline-start-color: var(--color-slate-900); |
| border-s-slate-950 | border-inline-start-color: var(--color-slate-950); |
| border-s-gray-50 | border-inline-start-color: var(--color-gray-50); |
| border-s-gray-100 | border-inline-start-color: var(--color-gray-100); |
| border-s-gray-200 | border-inline-start-color: var(--color-gray-200); |
| border-s-gray-300 | border-inline-start-color: var(--color-gray-300); |
| border-s-gray-400 | border-inline-start-color: var(--color-gray-400); |
| border-s-gray-500 | border-inline-start-color: var(--color-gray-500); |
| border-s-gray-600 | border-inline-start-color: var(--color-gray-600); |
| border-s-gray-700 | border-inline-start-color: var(--color-gray-700); |
| border-s-gray-800 | border-inline-start-color: var(--color-gray-800); |
| border-s-gray-900 | border-inline-start-color: var(--color-gray-900); |
| border-s-gray-950 | border-inline-start-color: var(--color-gray-950); |
| border-s-zinc-50 | border-inline-start-color: var(--color-zinc-50); |
| border-s-zinc-100 | border-inline-start-color: var(--color-zinc-100); |
| border-s-zinc-200 | border-inline-start-color: var(--color-zinc-200); |
| border-s-zinc-300 | border-inline-start-color: var(--color-zinc-300); |
| border-s-zinc-400 | border-inline-start-color: var(--color-zinc-400); |
| border-s-zinc-500 | border-inline-start-color: var(--color-zinc-500); |
| border-s-zinc-600 | border-inline-start-color: var(--color-zinc-600); |
| border-s-zinc-700 | border-inline-start-color: var(--color-zinc-700); |
| border-s-zinc-800 | border-inline-start-color: var(--color-zinc-800); |
| border-s-zinc-900 | border-inline-start-color: var(--color-zinc-900); |
| border-s-zinc-950 | border-inline-start-color: var(--color-zinc-950); |
| border-s-neutral-50 | border-inline-start-color: var(--color-neutral-50); |
| border-s-neutral-100 | border-inline-start-color: var(--color-neutral-100); |
| border-s-neutral-200 | border-inline-start-color: var(--color-neutral-200); |
| border-s-neutral-300 | border-inline-start-color: var(--color-neutral-300); |
| border-s-neutral-400 | border-inline-start-color: var(--color-neutral-400); |
| border-s-neutral-500 | border-inline-start-color: var(--color-neutral-500); |
| border-s-neutral-600 | border-inline-start-color: var(--color-neutral-600); |
| border-s-neutral-700 | border-inline-start-color: var(--color-neutral-700); |
| border-s-neutral-800 | border-inline-start-color: var(--color-neutral-800); |
| border-s-neutral-900 | border-inline-start-color: var(--color-neutral-900); |
| border-s-neutral-950 | border-inline-start-color: var(--color-neutral-950); |
| border-s-stone-50 | border-inline-start-color: var(--color-stone-50); |
| border-s-stone-100 | border-inline-start-color: var(--color-stone-100); |
| border-s-stone-200 | border-inline-start-color: var(--color-stone-200); |
| border-s-stone-300 | border-inline-start-color: var(--color-stone-300); |
| border-s-stone-400 | border-inline-start-color: var(--color-stone-400); |
| border-s-stone-500 | border-inline-start-color: var(--color-stone-500); |
| border-s-stone-600 | border-inline-start-color: var(--color-stone-600); |
| border-s-stone-700 | border-inline-start-color: var(--color-stone-700); |
| border-s-stone-800 | border-inline-start-color: var(--color-stone-800); |
| border-s-stone-900 | border-inline-start-color: var(--color-stone-900); |
| border-s-stone-950 | border-inline-start-color: var(--color-stone-950); |
| border-s-(<custom-property>) | border-inline-start-color: var(<custom-property>); |
| border-s-[<value>] | border-inline-start-color: <value>; |
| border-e-inherit | border-inline-end-color: inherit; |
| border-e-current | border-inline-end-color: currentColor; |
| border-e-transparent | border-inline-end-color: transparent; |
| border-e-black | border-inline-end-color: var(--color-black); /* #000 */ |
| border-e-white | border-inline-end-color: var(--color-white); /* #fff */ |
| border-e-red-50 | border-inline-end-color: var(--color-red-50); |
| border-e-red-100 | border-inline-end-color: var(--color-red-100); |
| border-e-red-200 | border-inline-end-color: var(--color-red-200); |
| border-e-red-300 | border-inline-end-color: var(--color-red-300); |
| border-e-red-400 | border-inline-end-color: var(--color-red-400); |
| border-e-red-500 | border-inline-end-color: var(--color-red-500); |
| border-e-red-600 | border-inline-end-color: var(--color-red-600); |
| border-e-red-700 | border-inline-end-color: var(--color-red-700); |
| border-e-red-800 | border-inline-end-color: var(--color-red-800); |
| border-e-red-900 | border-inline-end-color: var(--color-red-900); |
| border-e-red-950 | border-inline-end-color: var(--color-red-950); |
| border-e-orange-50 | border-inline-end-color: var(--color-orange-50); |
| border-e-orange-100 | border-inline-end-color: var(--color-orange-100); |
| border-e-orange-200 | border-inline-end-color: var(--color-orange-200); |
| border-e-orange-300 | border-inline-end-color: var(--color-orange-300); |
| border-e-orange-400 | border-inline-end-color: var(--color-orange-400); |
| border-e-orange-500 | border-inline-end-color: var(--color-orange-500); |
| border-e-orange-600 | border-inline-end-color: var(--color-orange-600); |
| border-e-orange-700 | border-inline-end-color: var(--color-orange-700); |
| border-e-orange-800 | border-inline-end-color: var(--color-orange-800); |
| border-e-orange-900 | border-inline-end-color: var(--color-orange-900); |
| border-e-orange-950 | border-inline-end-color: var(--color-orange-950); |
| border-e-amber-50 | border-inline-end-color: var(--color-amber-50); |
| border-e-amber-100 | border-inline-end-color: var(--color-amber-100); |
| border-e-amber-200 | border-inline-end-color: var(--color-amber-200); |
| border-e-amber-300 | border-inline-end-color: var(--color-amber-300); |
| border-e-amber-400 | border-inline-end-color: var(--color-amber-400); |
| border-e-amber-500 | border-inline-end-color: var(--color-amber-500); |
| border-e-amber-600 | border-inline-end-color: var(--color-amber-600); |
| border-e-amber-700 | border-inline-end-color: var(--color-amber-700); |
| border-e-amber-800 | border-inline-end-color: var(--color-amber-800); |
| border-e-amber-900 | border-inline-end-color: var(--color-amber-900); |
| border-e-amber-950 | border-inline-end-color: var(--color-amber-950); |
| border-e-yellow-50 | border-inline-end-color: var(--color-yellow-50); |
| border-e-yellow-100 | border-inline-end-color: var(--color-yellow-100); |
| border-e-yellow-200 | border-inline-end-color: var(--color-yellow-200); |
| border-e-yellow-300 | border-inline-end-color: var(--color-yellow-300); |
| border-e-yellow-400 | border-inline-end-color: var(--color-yellow-400); |
| border-e-yellow-500 | border-inline-end-color: var(--color-yellow-500); |
| border-e-yellow-600 | border-inline-end-color: var(--color-yellow-600); |
| border-e-yellow-700 | border-inline-end-color: var(--color-yellow-700); |
| border-e-yellow-800 | border-inline-end-color: var(--color-yellow-800); |
| border-e-yellow-900 | border-inline-end-color: var(--color-yellow-900); |
| border-e-yellow-950 | border-inline-end-color: var(--color-yellow-950); |
| border-e-lime-50 | border-inline-end-color: var(--color-lime-50); |
| border-e-lime-100 | border-inline-end-color: var(--color-lime-100); |
| border-e-lime-200 | border-inline-end-color: var(--color-lime-200); |
| border-e-lime-300 | border-inline-end-color: var(--color-lime-300); |
| border-e-lime-400 | border-inline-end-color: var(--color-lime-400); |
| border-e-lime-500 | border-inline-end-color: var(--color-lime-500); |
| border-e-lime-600 | border-inline-end-color: var(--color-lime-600); |
| border-e-lime-700 | border-inline-end-color: var(--color-lime-700); |
| border-e-lime-800 | border-inline-end-color: var(--color-lime-800); |
| border-e-lime-900 | border-inline-end-color: var(--color-lime-900); |
| border-e-lime-950 | border-inline-end-color: var(--color-lime-950); |
| border-e-green-50 | border-inline-end-color: var(--color-green-50); |
| border-e-green-100 | border-inline-end-color: var(--color-green-100); |
| border-e-green-200 | border-inline-end-color: var(--color-green-200); |
| border-e-green-300 | border-inline-end-color: var(--color-green-300); |
| border-e-green-400 | border-inline-end-color: var(--color-green-400); |
| border-e-green-500 | border-inline-end-color: var(--color-green-500); |
| border-e-green-600 | border-inline-end-color: var(--color-green-600); |
| border-e-green-700 | border-inline-end-color: var(--color-green-700); |
| border-e-green-800 | border-inline-end-color: var(--color-green-800); |
| border-e-green-900 | border-inline-end-color: var(--color-green-900); |
| border-e-green-950 | border-inline-end-color: var(--color-green-950); |
| border-e-emerald-50 | border-inline-end-color: var(--color-emerald-50); |
| border-e-emerald-100 | border-inline-end-color: var(--color-emerald-100); |
| border-e-emerald-200 | border-inline-end-color: var(--color-emerald-200); |
| border-e-emerald-300 | border-inline-end-color: var(--color-emerald-300); |
| border-e-emerald-400 | border-inline-end-color: var(--color-emerald-400); |
| border-e-emerald-500 | border-inline-end-color: var(--color-emerald-500); |
| border-e-emerald-600 | border-inline-end-color: var(--color-emerald-600); |
| border-e-emerald-700 | border-inline-end-color: var(--color-emerald-700); |
| border-e-emerald-800 | border-inline-end-color: var(--color-emerald-800); |
| border-e-emerald-900 | border-inline-end-color: var(--color-emerald-900); |
| border-e-emerald-950 | border-inline-end-color: var(--color-emerald-950); |
| border-e-teal-50 | border-inline-end-color: var(--color-teal-50); |
| border-e-teal-100 | border-inline-end-color: var(--color-teal-100); |
| border-e-teal-200 | border-inline-end-color: var(--color-teal-200); |
| border-e-teal-300 | border-inline-end-color: var(--color-teal-300); |
| border-e-teal-400 | border-inline-end-color: var(--color-teal-400); |
| border-e-teal-500 | border-inline-end-color: var(--color-teal-500); |
| border-e-teal-600 | border-inline-end-color: var(--color-teal-600); |
| border-e-teal-700 | border-inline-end-color: var(--color-teal-700); |
| border-e-teal-800 | border-inline-end-color: var(--color-teal-800); |
| border-e-teal-900 | border-inline-end-color: var(--color-teal-900); |
| border-e-teal-950 | border-inline-end-color: var(--color-teal-950); |
| border-e-cyan-50 | border-inline-end-color: var(--color-cyan-50); |
| border-e-cyan-100 | border-inline-end-color: var(--color-cyan-100); |
| border-e-cyan-200 | border-inline-end-color: var(--color-cyan-200); |
| border-e-cyan-300 | border-inline-end-color: var(--color-cyan-300); |
| border-e-cyan-400 | border-inline-end-color: var(--color-cyan-400); |
| border-e-cyan-500 | border-inline-end-color: var(--color-cyan-500); |
| border-e-cyan-600 | border-inline-end-color: var(--color-cyan-600); |
| border-e-cyan-700 | border-inline-end-color: var(--color-cyan-700); |
| border-e-cyan-800 | border-inline-end-color: var(--color-cyan-800); |
| border-e-cyan-900 | border-inline-end-color: var(--color-cyan-900); |
| border-e-cyan-950 | border-inline-end-color: var(--color-cyan-950); |
| border-e-sky-50 | border-inline-end-color: var(--color-sky-50); |
| border-e-sky-100 | border-inline-end-color: var(--color-sky-100); |
| border-e-sky-200 | border-inline-end-color: var(--color-sky-200); |
| border-e-sky-300 | border-inline-end-color: var(--color-sky-300); |
| border-e-sky-400 | border-inline-end-color: var(--color-sky-400); |
| border-e-sky-500 | border-inline-end-color: var(--color-sky-500); |
| border-e-sky-600 | border-inline-end-color: var(--color-sky-600); |
| border-e-sky-700 | border-inline-end-color: var(--color-sky-700); |
| border-e-sky-800 | border-inline-end-color: var(--color-sky-800); |
| border-e-sky-900 | border-inline-end-color: var(--color-sky-900); |
| border-e-sky-950 | border-inline-end-color: var(--color-sky-950); |
| border-e-blue-50 | border-inline-end-color: var(--color-blue-50); |
| border-e-blue-100 | border-inline-end-color: var(--color-blue-100); |
| border-e-blue-200 | border-inline-end-color: var(--color-blue-200); |
| border-e-blue-300 | border-inline-end-color: var(--color-blue-300); |
| border-e-blue-400 | border-inline-end-color: var(--color-blue-400); |
| border-e-blue-500 | border-inline-end-color: var(--color-blue-500); |
| border-e-blue-600 | border-inline-end-color: var(--color-blue-600); |
| border-e-blue-700 | border-inline-end-color: var(--color-blue-700); |
| border-e-blue-800 | border-inline-end-color: var(--color-blue-800); |
| border-e-blue-900 | border-inline-end-color: var(--color-blue-900); |
| border-e-blue-950 | border-inline-end-color: var(--color-blue-950); |
| border-e-indigo-50 | border-inline-end-color: var(--color-indigo-50); |
| border-e-indigo-100 | border-inline-end-color: var(--color-indigo-100); |
| border-e-indigo-200 | border-inline-end-color: var(--color-indigo-200); |
| border-e-indigo-300 | border-inline-end-color: var(--color-indigo-300); |
| border-e-indigo-400 | border-inline-end-color: var(--color-indigo-400); |
| border-e-indigo-500 | border-inline-end-color: var(--color-indigo-500); |
| border-e-indigo-600 | border-inline-end-color: var(--color-indigo-600); |
| border-e-indigo-700 | border-inline-end-color: var(--color-indigo-700); |
| border-e-indigo-800 | border-inline-end-color: var(--color-indigo-800); |
| border-e-indigo-900 | border-inline-end-color: var(--color-indigo-900); |
| border-e-indigo-950 | border-inline-end-color: var(--color-indigo-950); |
| border-e-violet-50 | border-inline-end-color: var(--color-violet-50); |
| border-e-violet-100 | border-inline-end-color: var(--color-violet-100); |
| border-e-violet-200 | border-inline-end-color: var(--color-violet-200); |
| border-e-violet-300 | border-inline-end-color: var(--color-violet-300); |
| border-e-violet-400 | border-inline-end-color: var(--color-violet-400); |
| border-e-violet-500 | border-inline-end-color: var(--color-violet-500); |
| border-e-violet-600 | border-inline-end-color: var(--color-violet-600); |
| border-e-violet-700 | border-inline-end-color: var(--color-violet-700); |
| border-e-violet-800 | border-inline-end-color: var(--color-violet-800); |
| border-e-violet-900 | border-inline-end-color: var(--color-violet-900); |
| border-e-violet-950 | border-inline-end-color: var(--color-violet-950); |
| border-e-purple-50 | border-inline-end-color: var(--color-purple-50); |
| border-e-purple-100 | border-inline-end-color: var(--color-purple-100); |
| border-e-purple-200 | border-inline-end-color: var(--color-purple-200); |
| border-e-purple-300 | border-inline-end-color: var(--color-purple-300); |
| border-e-purple-400 | border-inline-end-color: var(--color-purple-400); |
| border-e-purple-500 | border-inline-end-color: var(--color-purple-500); |
| border-e-purple-600 | border-inline-end-color: var(--color-purple-600); |
| border-e-purple-700 | border-inline-end-color: var(--color-purple-700); |
| border-e-purple-800 | border-inline-end-color: var(--color-purple-800); |
| border-e-purple-900 | border-inline-end-color: var(--color-purple-900); |
| border-e-purple-950 | border-inline-end-color: var(--color-purple-950); |
| border-e-fuchsia-50 | border-inline-end-color: var(--color-fuchsia-50); |
| border-e-fuchsia-100 | border-inline-end-color: var(--color-fuchsia-100); |
| border-e-fuchsia-200 | border-inline-end-color: var(--color-fuchsia-200); |
| border-e-fuchsia-300 | border-inline-end-color: var(--color-fuchsia-300); |
| border-e-fuchsia-400 | border-inline-end-color: var(--color-fuchsia-400); |
| border-e-fuchsia-500 | border-inline-end-color: var(--color-fuchsia-500); |
| border-e-fuchsia-600 | border-inline-end-color: var(--color-fuchsia-600); |
| border-e-fuchsia-700 | border-inline-end-color: var(--color-fuchsia-700); |
| border-e-fuchsia-800 | border-inline-end-color: var(--color-fuchsia-800); |
| border-e-fuchsia-900 | border-inline-end-color: var(--color-fuchsia-900); |
| border-e-fuchsia-950 | border-inline-end-color: var(--color-fuchsia-950); |
| border-e-pink-50 | border-inline-end-color: var(--color-pink-50); |
| border-e-pink-100 | border-inline-end-color: var(--color-pink-100); |
| border-e-pink-200 | border-inline-end-color: var(--color-pink-200); |
| border-e-pink-300 | border-inline-end-color: var(--color-pink-300); |
| border-e-pink-400 | border-inline-end-color: var(--color-pink-400); |
| border-e-pink-500 | border-inline-end-color: var(--color-pink-500); |
| border-e-pink-600 | border-inline-end-color: var(--color-pink-600); |
| border-e-pink-700 | border-inline-end-color: var(--color-pink-700); |
| border-e-pink-800 | border-inline-end-color: var(--color-pink-800); |
| border-e-pink-900 | border-inline-end-color: var(--color-pink-900); |
| border-e-pink-950 | border-inline-end-color: var(--color-pink-950); |
| border-e-rose-50 | border-inline-end-color: var(--color-rose-50); |
| border-e-rose-100 | border-inline-end-color: var(--color-rose-100); |
| border-e-rose-200 | border-inline-end-color: var(--color-rose-200); |
| border-e-rose-300 | border-inline-end-color: var(--color-rose-300); |
| border-e-rose-400 | border-inline-end-color: var(--color-rose-400); |
| border-e-rose-500 | border-inline-end-color: var(--color-rose-500); |
| border-e-rose-600 | border-inline-end-color: var(--color-rose-600); |
| border-e-rose-700 | border-inline-end-color: var(--color-rose-700); |
| border-e-rose-800 | border-inline-end-color: var(--color-rose-800); |
| border-e-rose-900 | border-inline-end-color: var(--color-rose-900); |
| border-e-rose-950 | border-inline-end-color: var(--color-rose-950); |
| border-e-slate-50 | border-inline-end-color: var(--color-slate-50); |
| border-e-slate-100 | border-inline-end-color: var(--color-slate-100); |
| border-e-slate-200 | border-inline-end-color: var(--color-slate-200); |
| border-e-slate-300 | border-inline-end-color: var(--color-slate-300); |
| border-e-slate-400 | border-inline-end-color: var(--color-slate-400); |
| border-e-slate-500 | border-inline-end-color: var(--color-slate-500); |
| border-e-slate-600 | border-inline-end-color: var(--color-slate-600); |
| border-e-slate-700 | border-inline-end-color: var(--color-slate-700); |
| border-e-slate-800 | border-inline-end-color: var(--color-slate-800); |
| border-e-slate-900 | border-inline-end-color: var(--color-slate-900); |
| border-e-slate-950 | border-inline-end-color: var(--color-slate-950); |
| border-e-gray-50 | border-inline-end-color: var(--color-gray-50); |
| border-e-gray-100 | border-inline-end-color: var(--color-gray-100); |
| border-e-gray-200 | border-inline-end-color: var(--color-gray-200); |
| border-e-gray-300 | border-inline-end-color: var(--color-gray-300); |
| border-e-gray-400 | border-inline-end-color: var(--color-gray-400); |
| border-e-gray-500 | border-inline-end-color: var(--color-gray-500); |
| border-e-gray-600 | border-inline-end-color: var(--color-gray-600); |
| border-e-gray-700 | border-inline-end-color: var(--color-gray-700); |
| border-e-gray-800 | border-inline-end-color: var(--color-gray-800); |
| border-e-gray-900 | border-inline-end-color: var(--color-gray-900); |
| border-e-gray-950 | border-inline-end-color: var(--color-gray-950); |
| border-e-zinc-50 | border-inline-end-color: var(--color-zinc-50); |
| border-e-zinc-100 | border-inline-end-color: var(--color-zinc-100); |
| border-e-zinc-200 | border-inline-end-color: var(--color-zinc-200); |
| border-e-zinc-300 | border-inline-end-color: var(--color-zinc-300); |
| border-e-zinc-400 | border-inline-end-color: var(--color-zinc-400); |
| border-e-zinc-500 | border-inline-end-color: var(--color-zinc-500); |
| border-e-zinc-600 | border-inline-end-color: var(--color-zinc-600); |
| border-e-zinc-700 | border-inline-end-color: var(--color-zinc-700); |
| border-e-zinc-800 | border-inline-end-color: var(--color-zinc-800); |
| border-e-zinc-900 | border-inline-end-color: var(--color-zinc-900); |
| border-e-zinc-950 | border-inline-end-color: var(--color-zinc-950); |
| border-e-neutral-50 | border-inline-end-color: var(--color-neutral-50); |
| border-e-neutral-100 | border-inline-end-color: var(--color-neutral-100); |
| border-e-neutral-200 | border-inline-end-color: var(--color-neutral-200); |
| border-e-neutral-300 | border-inline-end-color: var(--color-neutral-300); |
| border-e-neutral-400 | border-inline-end-color: var(--color-neutral-400); |
| border-e-neutral-500 | border-inline-end-color: var(--color-neutral-500); |
| border-e-neutral-600 | border-inline-end-color: var(--color-neutral-600); |
| border-e-neutral-700 | border-inline-end-color: var(--color-neutral-700); |
| border-e-neutral-800 | border-inline-end-color: var(--color-neutral-800); |
| border-e-neutral-900 | border-inline-end-color: var(--color-neutral-900); |
| border-e-neutral-950 | border-inline-end-color: var(--color-neutral-950); |
| border-e-stone-50 | border-inline-end-color: var(--color-stone-50); |
| border-e-stone-100 | border-inline-end-color: var(--color-stone-100); |
| border-e-stone-200 | border-inline-end-color: var(--color-stone-200); |
| border-e-stone-300 | border-inline-end-color: var(--color-stone-300); |
| border-e-stone-400 | border-inline-end-color: var(--color-stone-400); |
| border-e-stone-500 | border-inline-end-color: var(--color-stone-500); |
| border-e-stone-600 | border-inline-end-color: var(--color-stone-600); |
| border-e-stone-700 | border-inline-end-color: var(--color-stone-700); |
| border-e-stone-800 | border-inline-end-color: var(--color-stone-800); |
| border-e-stone-900 | border-inline-end-color: var(--color-stone-900); |
| border-e-stone-950 | border-inline-end-color: var(--color-stone-950); |
| border-e-(<custom-property>) | border-inline-end-color: var(<custom-property>); |
| border-e-[<value>] | border-inline-end-color: <value>; |
| border-t-inherit | border-top-color: inherit; |
| border-t-current | border-top-color: currentColor; |
| border-t-transparent | border-top-color: transparent; |
| border-t-black | border-top-color: var(--color-black); /* #000 */ |
| border-t-white | border-top-color: var(--color-white); /* #fff */ |
| border-t-red-50 | border-top-color: var(--color-red-50); |
| border-t-red-100 | border-top-color: var(--color-red-100); |
| border-t-red-200 | border-top-color: var(--color-red-200); |
| border-t-red-300 | border-top-color: var(--color-red-300); |
| border-t-red-400 | border-top-color: var(--color-red-400); |
| border-t-red-500 | border-top-color: var(--color-red-500); |
| border-t-red-600 | border-top-color: var(--color-red-600); |
| border-t-red-700 | border-top-color: var(--color-red-700); |
| border-t-red-800 | border-top-color: var(--color-red-800); |
| border-t-red-900 | border-top-color: var(--color-red-900); |
| border-t-red-950 | border-top-color: var(--color-red-950); |
| border-t-orange-50 | border-top-color: var(--color-orange-50); |
| border-t-orange-100 | border-top-color: var(--color-orange-100); |
| border-t-orange-200 | border-top-color: var(--color-orange-200); |
| border-t-orange-300 | border-top-color: var(--color-orange-300); |
| border-t-orange-400 | border-top-color: var(--color-orange-400); |
| border-t-orange-500 | border-top-color: var(--color-orange-500); |
| border-t-orange-600 | border-top-color: var(--color-orange-600); |
| border-t-orange-700 | border-top-color: var(--color-orange-700); |
| border-t-orange-800 | border-top-color: var(--color-orange-800); |
| border-t-orange-900 | border-top-color: var(--color-orange-900); |
| border-t-orange-950 | border-top-color: var(--color-orange-950); |
| border-t-amber-50 | border-top-color: var(--color-amber-50); |
| border-t-amber-100 | border-top-color: var(--color-amber-100); |
| border-t-amber-200 | border-top-color: var(--color-amber-200); |
| border-t-amber-300 | border-top-color: var(--color-amber-300); |
| border-t-amber-400 | border-top-color: var(--color-amber-400); |
| border-t-amber-500 | border-top-color: var(--color-amber-500); |
| border-t-amber-600 | border-top-color: var(--color-amber-600); |
| border-t-amber-700 | border-top-color: var(--color-amber-700); |
| border-t-amber-800 | border-top-color: var(--color-amber-800); |
| border-t-amber-900 | border-top-color: var(--color-amber-900); |
| border-t-amber-950 | border-top-color: var(--color-amber-950); |
| border-t-yellow-50 | border-top-color: var(--color-yellow-50); |
| border-t-yellow-100 | border-top-color: var(--color-yellow-100); |
| border-t-yellow-200 | border-top-color: var(--color-yellow-200); |
| border-t-yellow-300 | border-top-color: var(--color-yellow-300); |
| border-t-yellow-400 | border-top-color: var(--color-yellow-400); |
| border-t-yellow-500 | border-top-color: var(--color-yellow-500); |
| border-t-yellow-600 | border-top-color: var(--color-yellow-600); |
| border-t-yellow-700 | border-top-color: var(--color-yellow-700); |
| border-t-yellow-800 | border-top-color: var(--color-yellow-800); |
| border-t-yellow-900 | border-top-color: var(--color-yellow-900); |
| border-t-yellow-950 | border-top-color: var(--color-yellow-950); |
| border-t-lime-50 | border-top-color: var(--color-lime-50); |
| border-t-lime-100 | border-top-color: var(--color-lime-100); |
| border-t-lime-200 | border-top-color: var(--color-lime-200); |
| border-t-lime-300 | border-top-color: var(--color-lime-300); |
| border-t-lime-400 | border-top-color: var(--color-lime-400); |
| border-t-lime-500 | border-top-color: var(--color-lime-500); |
| border-t-lime-600 | border-top-color: var(--color-lime-600); |
| border-t-lime-700 | border-top-color: var(--color-lime-700); |
| border-t-lime-800 | border-top-color: var(--color-lime-800); |
| border-t-lime-900 | border-top-color: var(--color-lime-900); |
| border-t-lime-950 | border-top-color: var(--color-lime-950); |
| border-t-green-50 | border-top-color: var(--color-green-50); |
| border-t-green-100 | border-top-color: var(--color-green-100); |
| border-t-green-200 | border-top-color: var(--color-green-200); |
| border-t-green-300 | border-top-color: var(--color-green-300); |
| border-t-green-400 | border-top-color: var(--color-green-400); |
| border-t-green-500 | border-top-color: var(--color-green-500); |
| border-t-green-600 | border-top-color: var(--color-green-600); |
| border-t-green-700 | border-top-color: var(--color-green-700); |
| border-t-green-800 | border-top-color: var(--color-green-800); |
| border-t-green-900 | border-top-color: var(--color-green-900); |
| border-t-green-950 | border-top-color: var(--color-green-950); |
| border-t-emerald-50 | border-top-color: var(--color-emerald-50); |
| border-t-emerald-100 | border-top-color: var(--color-emerald-100); |
| border-t-emerald-200 | border-top-color: var(--color-emerald-200); |
| border-t-emerald-300 | border-top-color: var(--color-emerald-300); |
| border-t-emerald-400 | border-top-color: var(--color-emerald-400); |
| border-t-emerald-500 | border-top-color: var(--color-emerald-500); |
| border-t-emerald-600 | border-top-color: var(--color-emerald-600); |
| border-t-emerald-700 | border-top-color: var(--color-emerald-700); |
| border-t-emerald-800 | border-top-color: var(--color-emerald-800); |
| border-t-emerald-900 | border-top-color: var(--color-emerald-900); |
| border-t-emerald-950 | border-top-color: var(--color-emerald-950); |
| border-t-teal-50 | border-top-color: var(--color-teal-50); |
| border-t-teal-100 | border-top-color: var(--color-teal-100); |
| border-t-teal-200 | border-top-color: var(--color-teal-200); |
| border-t-teal-300 | border-top-color: var(--color-teal-300); |
| border-t-teal-400 | border-top-color: var(--color-teal-400); |
| border-t-teal-500 | border-top-color: var(--color-teal-500); |
| border-t-teal-600 | border-top-color: var(--color-teal-600); |
| border-t-teal-700 | border-top-color: var(--color-teal-700); |
| border-t-teal-800 | border-top-color: var(--color-teal-800); |
| border-t-teal-900 | border-top-color: var(--color-teal-900); |
| border-t-teal-950 | border-top-color: var(--color-teal-950); |
| border-t-cyan-50 | border-top-color: var(--color-cyan-50); |
| border-t-cyan-100 | border-top-color: var(--color-cyan-100); |
| border-t-cyan-200 | border-top-color: var(--color-cyan-200); |
| border-t-cyan-300 | border-top-color: var(--color-cyan-300); |
| border-t-cyan-400 | border-top-color: var(--color-cyan-400); |
| border-t-cyan-500 | border-top-color: var(--color-cyan-500); |
| border-t-cyan-600 | border-top-color: var(--color-cyan-600); |
| border-t-cyan-700 | border-top-color: var(--color-cyan-700); |
| border-t-cyan-800 | border-top-color: var(--color-cyan-800); |
| border-t-cyan-900 | border-top-color: var(--color-cyan-900); |
| border-t-cyan-950 | border-top-color: var(--color-cyan-950); |
| border-t-sky-50 | border-top-color: var(--color-sky-50); |
| border-t-sky-100 | border-top-color: var(--color-sky-100); |
| border-t-sky-200 | border-top-color: var(--color-sky-200); |
| border-t-sky-300 | border-top-color: var(--color-sky-300); |
| border-t-sky-400 | border-top-color: var(--color-sky-400); |
| border-t-sky-500 | border-top-color: var(--color-sky-500); |
| border-t-sky-600 | border-top-color: var(--color-sky-600); |
| border-t-sky-700 | border-top-color: var(--color-sky-700); |
| border-t-sky-800 | border-top-color: var(--color-sky-800); |
| border-t-sky-900 | border-top-color: var(--color-sky-900); |
| border-t-sky-950 | border-top-color: var(--color-sky-950); |
| border-t-blue-50 | border-top-color: var(--color-blue-50); |
| border-t-blue-100 | border-top-color: var(--color-blue-100); |
| border-t-blue-200 | border-top-color: var(--color-blue-200); |
| border-t-blue-300 | border-top-color: var(--color-blue-300); |
| border-t-blue-400 | border-top-color: var(--color-blue-400); |
| border-t-blue-500 | border-top-color: var(--color-blue-500); |
| border-t-blue-600 | border-top-color: var(--color-blue-600); |
| border-t-blue-700 | border-top-color: var(--color-blue-700); |
| border-t-blue-800 | border-top-color: var(--color-blue-800); |
| border-t-blue-900 | border-top-color: var(--color-blue-900); |
| border-t-blue-950 | border-top-color: var(--color-blue-950); |
| border-t-indigo-50 | border-top-color: var(--color-indigo-50); |
| border-t-indigo-100 | border-top-color: var(--color-indigo-100); |
| border-t-indigo-200 | border-top-color: var(--color-indigo-200); |
| border-t-indigo-300 | border-top-color: var(--color-indigo-300); |
| border-t-indigo-400 | border-top-color: var(--color-indigo-400); |
| border-t-indigo-500 | border-top-color: var(--color-indigo-500); |
| border-t-indigo-600 | border-top-color: var(--color-indigo-600); |
| border-t-indigo-700 | border-top-color: var(--color-indigo-700); |
| border-t-indigo-800 | border-top-color: var(--color-indigo-800); |
| border-t-indigo-900 | border-top-color: var(--color-indigo-900); |
| border-t-indigo-950 | border-top-color: var(--color-indigo-950); |
| border-t-violet-50 | border-top-color: var(--color-violet-50); |
| border-t-violet-100 | border-top-color: var(--color-violet-100); |
| border-t-violet-200 | border-top-color: var(--color-violet-200); |
| border-t-violet-300 | border-top-color: var(--color-violet-300); |
| border-t-violet-400 | border-top-color: var(--color-violet-400); |
| border-t-violet-500 | border-top-color: var(--color-violet-500); |
| border-t-violet-600 | border-top-color: var(--color-violet-600); |
| border-t-violet-700 | border-top-color: var(--color-violet-700); |
| border-t-violet-800 | border-top-color: var(--color-violet-800); |
| border-t-violet-900 | border-top-color: var(--color-violet-900); |
| border-t-violet-950 | border-top-color: var(--color-violet-950); |
| border-t-purple-50 | border-top-color: var(--color-purple-50); |
| border-t-purple-100 | border-top-color: var(--color-purple-100); |
| border-t-purple-200 | border-top-color: var(--color-purple-200); |
| border-t-purple-300 | border-top-color: var(--color-purple-300); |
| border-t-purple-400 | border-top-color: var(--color-purple-400); |
| border-t-purple-500 | border-top-color: var(--color-purple-500); |
| border-t-purple-600 | border-top-color: var(--color-purple-600); |
| border-t-purple-700 | border-top-color: var(--color-purple-700); |
| border-t-purple-800 | border-top-color: var(--color-purple-800); |
| border-t-purple-900 | border-top-color: var(--color-purple-900); |
| border-t-purple-950 | border-top-color: var(--color-purple-950); |
| border-t-fuchsia-50 | border-top-color: var(--color-fuchsia-50); |
| border-t-fuchsia-100 | border-top-color: var(--color-fuchsia-100); |
| border-t-fuchsia-200 | border-top-color: var(--color-fuchsia-200); |
| border-t-fuchsia-300 | border-top-color: var(--color-fuchsia-300); |
| border-t-fuchsia-400 | border-top-color: var(--color-fuchsia-400); |
| border-t-fuchsia-500 | border-top-color: var(--color-fuchsia-500); |
| border-t-fuchsia-600 | border-top-color: var(--color-fuchsia-600); |
| border-t-fuchsia-700 | border-top-color: var(--color-fuchsia-700); |
| border-t-fuchsia-800 | border-top-color: var(--color-fuchsia-800); |
| border-t-fuchsia-900 | border-top-color: var(--color-fuchsia-900); |
| border-t-fuchsia-950 | border-top-color: var(--color-fuchsia-950); |
| border-t-pink-50 | border-top-color: var(--color-pink-50); |
| border-t-pink-100 | border-top-color: var(--color-pink-100); |
| border-t-pink-200 | border-top-color: var(--color-pink-200); |
| border-t-pink-300 | border-top-color: var(--color-pink-300); |
| border-t-pink-400 | border-top-color: var(--color-pink-400); |
| border-t-pink-500 | border-top-color: var(--color-pink-500); |
| border-t-pink-600 | border-top-color: var(--color-pink-600); |
| border-t-pink-700 | border-top-color: var(--color-pink-700); |
| border-t-pink-800 | border-top-color: var(--color-pink-800); |
| border-t-pink-900 | border-top-color: var(--color-pink-900); |
| border-t-pink-950 | border-top-color: var(--color-pink-950); |
| border-t-rose-50 | border-top-color: var(--color-rose-50); |
| border-t-rose-100 | border-top-color: var(--color-rose-100); |
| border-t-rose-200 | border-top-color: var(--color-rose-200); |
| border-t-rose-300 | border-top-color: var(--color-rose-300); |
| border-t-rose-400 | border-top-color: var(--color-rose-400); |
| border-t-rose-500 | border-top-color: var(--color-rose-500); |
| border-t-rose-600 | border-top-color: var(--color-rose-600); |
| border-t-rose-700 | border-top-color: var(--color-rose-700); |
| border-t-rose-800 | border-top-color: var(--color-rose-800); |
| border-t-rose-900 | border-top-color: var(--color-rose-900); |
| border-t-rose-950 | border-top-color: var(--color-rose-950); |
| border-t-slate-50 | border-top-color: var(--color-slate-50); |
| border-t-slate-100 | border-top-color: var(--color-slate-100); |
| border-t-slate-200 | border-top-color: var(--color-slate-200); |
| border-t-slate-300 | border-top-color: var(--color-slate-300); |
| border-t-slate-400 | border-top-color: var(--color-slate-400); |
| border-t-slate-500 | border-top-color: var(--color-slate-500); |
| border-t-slate-600 | border-top-color: var(--color-slate-600); |
| border-t-slate-700 | border-top-color: var(--color-slate-700); |
| border-t-slate-800 | border-top-color: var(--color-slate-800); |
| border-t-slate-900 | border-top-color: var(--color-slate-900); |
| border-t-slate-950 | border-top-color: var(--color-slate-950); |
| border-t-gray-50 | border-top-color: var(--color-gray-50); |
| border-t-gray-100 | border-top-color: var(--color-gray-100); |
| border-t-gray-200 | border-top-color: var(--color-gray-200); |
| border-t-gray-300 | border-top-color: var(--color-gray-300); |
| border-t-gray-400 | border-top-color: var(--color-gray-400); |
| border-t-gray-500 | border-top-color: var(--color-gray-500); |
| border-t-gray-600 | border-top-color: var(--color-gray-600); |
| border-t-gray-700 | border-top-color: var(--color-gray-700); |
| border-t-gray-800 | border-top-color: var(--color-gray-800); |
| border-t-gray-900 | border-top-color: var(--color-gray-900); |
| border-t-gray-950 | border-top-color: var(--color-gray-950); |
| border-t-zinc-50 | border-top-color: var(--color-zinc-50); |
| border-t-zinc-100 | border-top-color: var(--color-zinc-100); |
| border-t-zinc-200 | border-top-color: var(--color-zinc-200); |
| border-t-zinc-300 | border-top-color: var(--color-zinc-300); |
| border-t-zinc-400 | border-top-color: var(--color-zinc-400); |
| border-t-zinc-500 | border-top-color: var(--color-zinc-500); |
| border-t-zinc-600 | border-top-color: var(--color-zinc-600); |
| border-t-zinc-700 | border-top-color: var(--color-zinc-700); |
| border-t-zinc-800 | border-top-color: var(--color-zinc-800); |
| border-t-zinc-900 | border-top-color: var(--color-zinc-900); |
| border-t-zinc-950 | border-top-color: var(--color-zinc-950); |
| border-t-neutral-50 | border-top-color: var(--color-neutral-50); |
| border-t-neutral-100 | border-top-color: var(--color-neutral-100); |
| border-t-neutral-200 | border-top-color: var(--color-neutral-200); |
| border-t-neutral-300 | border-top-color: var(--color-neutral-300); |
| border-t-neutral-400 | border-top-color: var(--color-neutral-400); |
| border-t-neutral-500 | border-top-color: var(--color-neutral-500); |
| border-t-neutral-600 | border-top-color: var(--color-neutral-600); |
| border-t-neutral-700 | border-top-color: var(--color-neutral-700); |
| border-t-neutral-800 | border-top-color: var(--color-neutral-800); |
| border-t-neutral-900 | border-top-color: var(--color-neutral-900); |
| border-t-neutral-950 | border-top-color: var(--color-neutral-950); |
| border-t-stone-50 | border-top-color: var(--color-stone-50); |
| border-t-stone-100 | border-top-color: var(--color-stone-100); |
| border-t-stone-200 | border-top-color: var(--color-stone-200); |
| border-t-stone-300 | border-top-color: var(--color-stone-300); |
| border-t-stone-400 | border-top-color: var(--color-stone-400); |
| border-t-stone-500 | border-top-color: var(--color-stone-500); |
| border-t-stone-600 | border-top-color: var(--color-stone-600); |
| border-t-stone-700 | border-top-color: var(--color-stone-700); |
| border-t-stone-800 | border-top-color: var(--color-stone-800); |
| border-t-stone-900 | border-top-color: var(--color-stone-900); |
| border-t-stone-950 | border-top-color: var(--color-stone-950); |
| border-t-(<custom-property>) | border-top-color: var(<custom-property>); |
| border-t-[<value>] | border-top-color: <value>; |
| border-r-inherit | border-right-color: inherit; |
| border-r-current | border-right-color: currentColor; |
| border-r-transparent | border-right-color: transparent; |
| border-r-black | border-right-color: var(--color-black); /* #000 */ |
| border-r-white | border-right-color: var(--color-white); /* #fff */ |
| border-r-red-50 | border-right-color: var(--color-red-50); |
| border-r-red-100 | border-right-color: var(--color-red-100); |
| border-r-red-200 | border-right-color: var(--color-red-200); |
| border-r-red-300 | border-right-color: var(--color-red-300); |
| border-r-red-400 | border-right-color: var(--color-red-400); |
| border-r-red-500 | border-right-color: var(--color-red-500); |
| border-r-red-600 | border-right-color: var(--color-red-600); |
| border-r-red-700 | border-right-color: var(--color-red-700); |
| border-r-red-800 | border-right-color: var(--color-red-800); |
| border-r-red-900 | border-right-color: var(--color-red-900); |
| border-r-red-950 | border-right-color: var(--color-red-950); |
| border-r-orange-50 | border-right-color: var(--color-orange-50); |
| border-r-orange-100 | border-right-color: var(--color-orange-100); |
| border-r-orange-200 | border-right-color: var(--color-orange-200); |
| border-r-orange-300 | border-right-color: var(--color-orange-300); |
| border-r-orange-400 | border-right-color: var(--color-orange-400); |
| border-r-orange-500 | border-right-color: var(--color-orange-500); |
| border-r-orange-600 | border-right-color: var(--color-orange-600); |
| border-r-orange-700 | border-right-color: var(--color-orange-700); |
| border-r-orange-800 | border-right-color: var(--color-orange-800); |
| border-r-orange-900 | border-right-color: var(--color-orange-900); |
| border-r-orange-950 | border-right-color: var(--color-orange-950); |
| border-r-amber-50 | border-right-color: var(--color-amber-50); |
| border-r-amber-100 | border-right-color: var(--color-amber-100); |
| border-r-amber-200 | border-right-color: var(--color-amber-200); |
| border-r-amber-300 | border-right-color: var(--color-amber-300); |
| border-r-amber-400 | border-right-color: var(--color-amber-400); |
| border-r-amber-500 | border-right-color: var(--color-amber-500); |
| border-r-amber-600 | border-right-color: var(--color-amber-600); |
| border-r-amber-700 | border-right-color: var(--color-amber-700); |
| border-r-amber-800 | border-right-color: var(--color-amber-800); |
| border-r-amber-900 | border-right-color: var(--color-amber-900); |
| border-r-amber-950 | border-right-color: var(--color-amber-950); |
| border-r-yellow-50 | border-right-color: var(--color-yellow-50); |
| border-r-yellow-100 | border-right-color: var(--color-yellow-100); |
| border-r-yellow-200 | border-right-color: var(--color-yellow-200); |
| border-r-yellow-300 | border-right-color: var(--color-yellow-300); |
| border-r-yellow-400 | border-right-color: var(--color-yellow-400); |
| border-r-yellow-500 | border-right-color: var(--color-yellow-500); |
| border-r-yellow-600 | border-right-color: var(--color-yellow-600); |
| border-r-yellow-700 | border-right-color: var(--color-yellow-700); |
| border-r-yellow-800 | border-right-color: var(--color-yellow-800); |
| border-r-yellow-900 | border-right-color: var(--color-yellow-900); |
| border-r-yellow-950 | border-right-color: var(--color-yellow-950); |
| border-r-lime-50 | border-right-color: var(--color-lime-50); |
| border-r-lime-100 | border-right-color: var(--color-lime-100); |
| border-r-lime-200 | border-right-color: var(--color-lime-200); |
| border-r-lime-300 | border-right-color: var(--color-lime-300); |
| border-r-lime-400 | border-right-color: var(--color-lime-400); |
| border-r-lime-500 | border-right-color: var(--color-lime-500); |
| border-r-lime-600 | border-right-color: var(--color-lime-600); |
| border-r-lime-700 | border-right-color: var(--color-lime-700); |
| border-r-lime-800 | border-right-color: var(--color-lime-800); |
| border-r-lime-900 | border-right-color: var(--color-lime-900); |
| border-r-lime-950 | border-right-color: var(--color-lime-950); |
| border-r-green-50 | border-right-color: var(--color-green-50); |
| border-r-green-100 | border-right-color: var(--color-green-100); |
| border-r-green-200 | border-right-color: var(--color-green-200); |
| border-r-green-300 | border-right-color: var(--color-green-300); |
| border-r-green-400 | border-right-color: var(--color-green-400); |
| border-r-green-500 | border-right-color: var(--color-green-500); |
| border-r-green-600 | border-right-color: var(--color-green-600); |
| border-r-green-700 | border-right-color: var(--color-green-700); |
| border-r-green-800 | border-right-color: var(--color-green-800); |
| border-r-green-900 | border-right-color: var(--color-green-900); |
| border-r-green-950 | border-right-color: var(--color-green-950); |
| border-r-emerald-50 | border-right-color: var(--color-emerald-50); |
| border-r-emerald-100 | border-right-color: var(--color-emerald-100); |
| border-r-emerald-200 | border-right-color: var(--color-emerald-200); |
| border-r-emerald-300 | border-right-color: var(--color-emerald-300); |
| border-r-emerald-400 | border-right-color: var(--color-emerald-400); |
| border-r-emerald-500 | border-right-color: var(--color-emerald-500); |
| border-r-emerald-600 | border-right-color: var(--color-emerald-600); |
| border-r-emerald-700 | border-right-color: var(--color-emerald-700); |
| border-r-emerald-800 | border-right-color: var(--color-emerald-800); |
| border-r-emerald-900 | border-right-color: var(--color-emerald-900); |
| border-r-emerald-950 | border-right-color: var(--color-emerald-950); |
| border-r-teal-50 | border-right-color: var(--color-teal-50); |
| border-r-teal-100 | border-right-color: var(--color-teal-100); |
| border-r-teal-200 | border-right-color: var(--color-teal-200); |
| border-r-teal-300 | border-right-color: var(--color-teal-300); |
| border-r-teal-400 | border-right-color: var(--color-teal-400); |
| border-r-teal-500 | border-right-color: var(--color-teal-500); |
| border-r-teal-600 | border-right-color: var(--color-teal-600); |
| border-r-teal-700 | border-right-color: var(--color-teal-700); |
| border-r-teal-800 | border-right-color: var(--color-teal-800); |
| border-r-teal-900 | border-right-color: var(--color-teal-900); |
| border-r-teal-950 | border-right-color: var(--color-teal-950); |
| border-r-cyan-50 | border-right-color: var(--color-cyan-50); |
| border-r-cyan-100 | border-right-color: var(--color-cyan-100); |
| border-r-cyan-200 | border-right-color: var(--color-cyan-200); |
| border-r-cyan-300 | border-right-color: var(--color-cyan-300); |
| border-r-cyan-400 | border-right-color: var(--color-cyan-400); |
| border-r-cyan-500 | border-right-color: var(--color-cyan-500); |
| border-r-cyan-600 | border-right-color: var(--color-cyan-600); |
| border-r-cyan-700 | border-right-color: var(--color-cyan-700); |
| border-r-cyan-800 | border-right-color: var(--color-cyan-800); |
| border-r-cyan-900 | border-right-color: var(--color-cyan-900); |
| border-r-cyan-950 | border-right-color: var(--color-cyan-950); |
| border-r-sky-50 | border-right-color: var(--color-sky-50); |
| border-r-sky-100 | border-right-color: var(--color-sky-100); |
| border-r-sky-200 | border-right-color: var(--color-sky-200); |
| border-r-sky-300 | border-right-color: var(--color-sky-300); |
| border-r-sky-400 | border-right-color: var(--color-sky-400); |
| border-r-sky-500 | border-right-color: var(--color-sky-500); |
| border-r-sky-600 | border-right-color: var(--color-sky-600); |
| border-r-sky-700 | border-right-color: var(--color-sky-700); |
| border-r-sky-800 | border-right-color: var(--color-sky-800); |
| border-r-sky-900 | border-right-color: var(--color-sky-900); |
| border-r-sky-950 | border-right-color: var(--color-sky-950); |
| border-r-blue-50 | border-right-color: var(--color-blue-50); |
| border-r-blue-100 | border-right-color: var(--color-blue-100); |
| border-r-blue-200 | border-right-color: var(--color-blue-200); |
| border-r-blue-300 | border-right-color: var(--color-blue-300); |
| border-r-blue-400 | border-right-color: var(--color-blue-400); |
| border-r-blue-500 | border-right-color: var(--color-blue-500); |
| border-r-blue-600 | border-right-color: var(--color-blue-600); |
| border-r-blue-700 | border-right-color: var(--color-blue-700); |
| border-r-blue-800 | border-right-color: var(--color-blue-800); |
| border-r-blue-900 | border-right-color: var(--color-blue-900); |
| border-r-blue-950 | border-right-color: var(--color-blue-950); |
| border-r-indigo-50 | border-right-color: var(--color-indigo-50); |
| border-r-indigo-100 | border-right-color: var(--color-indigo-100); |
| border-r-indigo-200 | border-right-color: var(--color-indigo-200); |
| border-r-indigo-300 | border-right-color: var(--color-indigo-300); |
| border-r-indigo-400 | border-right-color: var(--color-indigo-400); |
| border-r-indigo-500 | border-right-color: var(--color-indigo-500); |
| border-r-indigo-600 | border-right-color: var(--color-indigo-600); |
| border-r-indigo-700 | border-right-color: var(--color-indigo-700); |
| border-r-indigo-800 | border-right-color: var(--color-indigo-800); |
| border-r-indigo-900 | border-right-color: var(--color-indigo-900); |
| border-r-indigo-950 | border-right-color: var(--color-indigo-950); |
| border-r-violet-50 | border-right-color: var(--color-violet-50); |
| border-r-violet-100 | border-right-color: var(--color-violet-100); |
| border-r-violet-200 | border-right-color: var(--color-violet-200); |
| border-r-violet-300 | border-right-color: var(--color-violet-300); |
| border-r-violet-400 | border-right-color: var(--color-violet-400); |
| border-r-violet-500 | border-right-color: var(--color-violet-500); |
| border-r-violet-600 | border-right-color: var(--color-violet-600); |
| border-r-violet-700 | border-right-color: var(--color-violet-700); |
| border-r-violet-800 | border-right-color: var(--color-violet-800); |
| border-r-violet-900 | border-right-color: var(--color-violet-900); |
| border-r-violet-950 | border-right-color: var(--color-violet-950); |
| border-r-purple-50 | border-right-color: var(--color-purple-50); |
| border-r-purple-100 | border-right-color: var(--color-purple-100); |
| border-r-purple-200 | border-right-color: var(--color-purple-200); |
| border-r-purple-300 | border-right-color: var(--color-purple-300); |
| border-r-purple-400 | border-right-color: var(--color-purple-400); |
| border-r-purple-500 | border-right-color: var(--color-purple-500); |
| border-r-purple-600 | border-right-color: var(--color-purple-600); |
| border-r-purple-700 | border-right-color: var(--color-purple-700); |
| border-r-purple-800 | border-right-color: var(--color-purple-800); |
| border-r-purple-900 | border-right-color: var(--color-purple-900); |
| border-r-purple-950 | border-right-color: var(--color-purple-950); |
| border-r-fuchsia-50 | border-right-color: var(--color-fuchsia-50); |
| border-r-fuchsia-100 | border-right-color: var(--color-fuchsia-100); |
| border-r-fuchsia-200 | border-right-color: var(--color-fuchsia-200); |
| border-r-fuchsia-300 | border-right-color: var(--color-fuchsia-300); |
| border-r-fuchsia-400 | border-right-color: var(--color-fuchsia-400); |
| border-r-fuchsia-500 | border-right-color: var(--color-fuchsia-500); |
| border-r-fuchsia-600 | border-right-color: var(--color-fuchsia-600); |
| border-r-fuchsia-700 | border-right-color: var(--color-fuchsia-700); |
| border-r-fuchsia-800 | border-right-color: var(--color-fuchsia-800); |
| border-r-fuchsia-900 | border-right-color: var(--color-fuchsia-900); |
| border-r-fuchsia-950 | border-right-color: var(--color-fuchsia-950); |
| border-r-pink-50 | border-right-color: var(--color-pink-50); |
| border-r-pink-100 | border-right-color: var(--color-pink-100); |
| border-r-pink-200 | border-right-color: var(--color-pink-200); |
| border-r-pink-300 | border-right-color: var(--color-pink-300); |
| border-r-pink-400 | border-right-color: var(--color-pink-400); |
| border-r-pink-500 | border-right-color: var(--color-pink-500); |
| border-r-pink-600 | border-right-color: var(--color-pink-600); |
| border-r-pink-700 | border-right-color: var(--color-pink-700); |
| border-r-pink-800 | border-right-color: var(--color-pink-800); |
| border-r-pink-900 | border-right-color: var(--color-pink-900); |
| border-r-pink-950 | border-right-color: var(--color-pink-950); |
| border-r-rose-50 | border-right-color: var(--color-rose-50); |
| border-r-rose-100 | border-right-color: var(--color-rose-100); |
| border-r-rose-200 | border-right-color: var(--color-rose-200); |
| border-r-rose-300 | border-right-color: var(--color-rose-300); |
| border-r-rose-400 | border-right-color: var(--color-rose-400); |
| border-r-rose-500 | border-right-color: var(--color-rose-500); |
| border-r-rose-600 | border-right-color: var(--color-rose-600); |
| border-r-rose-700 | border-right-color: var(--color-rose-700); |
| border-r-rose-800 | border-right-color: var(--color-rose-800); |
| border-r-rose-900 | border-right-color: var(--color-rose-900); |
| border-r-rose-950 | border-right-color: var(--color-rose-950); |
| border-r-slate-50 | border-right-color: var(--color-slate-50); |
| border-r-slate-100 | border-right-color: var(--color-slate-100); |
| border-r-slate-200 | border-right-color: var(--color-slate-200); |
| border-r-slate-300 | border-right-color: var(--color-slate-300); |
| border-r-slate-400 | border-right-color: var(--color-slate-400); |
| border-r-slate-500 | border-right-color: var(--color-slate-500); |
| border-r-slate-600 | border-right-color: var(--color-slate-600); |
| border-r-slate-700 | border-right-color: var(--color-slate-700); |
| border-r-slate-800 | border-right-color: var(--color-slate-800); |
| border-r-slate-900 | border-right-color: var(--color-slate-900); |
| border-r-slate-950 | border-right-color: var(--color-slate-950); |
| border-r-gray-50 | border-right-color: var(--color-gray-50); |
| border-r-gray-100 | border-right-color: var(--color-gray-100); |
| border-r-gray-200 | border-right-color: var(--color-gray-200); |
| border-r-gray-300 | border-right-color: var(--color-gray-300); |
| border-r-gray-400 | border-right-color: var(--color-gray-400); |
| border-r-gray-500 | border-right-color: var(--color-gray-500); |
| border-r-gray-600 | border-right-color: var(--color-gray-600); |
| border-r-gray-700 | border-right-color: var(--color-gray-700); |
| border-r-gray-800 | border-right-color: var(--color-gray-800); |
| border-r-gray-900 | border-right-color: var(--color-gray-900); |
| border-r-gray-950 | border-right-color: var(--color-gray-950); |
| border-r-zinc-50 | border-right-color: var(--color-zinc-50); |
| border-r-zinc-100 | border-right-color: var(--color-zinc-100); |
| border-r-zinc-200 | border-right-color: var(--color-zinc-200); |
| border-r-zinc-300 | border-right-color: var(--color-zinc-300); |
| border-r-zinc-400 | border-right-color: var(--color-zinc-400); |
| border-r-zinc-500 | border-right-color: var(--color-zinc-500); |
| border-r-zinc-600 | border-right-color: var(--color-zinc-600); |
| border-r-zinc-700 | border-right-color: var(--color-zinc-700); |
| border-r-zinc-800 | border-right-color: var(--color-zinc-800); |
| border-r-zinc-900 | border-right-color: var(--color-zinc-900); |
| border-r-zinc-950 | border-right-color: var(--color-zinc-950); |
| border-r-neutral-50 | border-right-color: var(--color-neutral-50); |
| border-r-neutral-100 | border-right-color: var(--color-neutral-100); |
| border-r-neutral-200 | border-right-color: var(--color-neutral-200); |
| border-r-neutral-300 | border-right-color: var(--color-neutral-300); |
| border-r-neutral-400 | border-right-color: var(--color-neutral-400); |
| border-r-neutral-500 | border-right-color: var(--color-neutral-500); |
| border-r-neutral-600 | border-right-color: var(--color-neutral-600); |
| border-r-neutral-700 | border-right-color: var(--color-neutral-700); |
| border-r-neutral-800 | border-right-color: var(--color-neutral-800); |
| border-r-neutral-900 | border-right-color: var(--color-neutral-900); |
| border-r-neutral-950 | border-right-color: var(--color-neutral-950); |
| border-r-stone-50 | border-right-color: var(--color-stone-50); |
| border-r-stone-100 | border-right-color: var(--color-stone-100); |
| border-r-stone-200 | border-right-color: var(--color-stone-200); |
| border-r-stone-300 | border-right-color: var(--color-stone-300); |
| border-r-stone-400 | border-right-color: var(--color-stone-400); |
| border-r-stone-500 | border-right-color: var(--color-stone-500); |
| border-r-stone-600 | border-right-color: var(--color-stone-600); |
| border-r-stone-700 | border-right-color: var(--color-stone-700); |
| border-r-stone-800 | border-right-color: var(--color-stone-800); |
| border-r-stone-900 | border-right-color: var(--color-stone-900); |
| border-r-stone-950 | border-right-color: var(--color-stone-950); |
| border-r-(<custom-property>) | border-right-color: var(<custom-property>); |
| border-r-[<value>] | border-right-color: <value>; |
| border-b-inherit | border-bottom-color: inherit; |
| border-b-current | border-bottom-color: currentColor; |
| border-b-transparent | border-bottom-color: transparent; |
| border-b-black | border-bottom-color: var(--color-black); /* #000 */ |
| border-b-white | border-bottom-color: var(--color-white); /* #fff */ |
| border-b-red-50 | border-bottom-color: var(--color-red-50); |
| border-b-red-100 | border-bottom-color: var(--color-red-100); |
| border-b-red-200 | border-bottom-color: var(--color-red-200); |
| border-b-red-300 | border-bottom-color: var(--color-red-300); |
| border-b-red-400 | border-bottom-color: var(--color-red-400); |
| border-b-red-500 | border-bottom-color: var(--color-red-500); |
| border-b-red-600 | border-bottom-color: var(--color-red-600); |
| border-b-red-700 | border-bottom-color: var(--color-red-700); |
| border-b-red-800 | border-bottom-color: var(--color-red-800); |
| border-b-red-900 | border-bottom-color: var(--color-red-900); |
| border-b-red-950 | border-bottom-color: var(--color-red-950); |
| border-b-orange-50 | border-bottom-color: var(--color-orange-50); |
| border-b-orange-100 | border-bottom-color: var(--color-orange-100); |
| border-b-orange-200 | border-bottom-color: var(--color-orange-200); |
| border-b-orange-300 | border-bottom-color: var(--color-orange-300); |
| border-b-orange-400 | border-bottom-color: var(--color-orange-400); |
| border-b-orange-500 | border-bottom-color: var(--color-orange-500); |
| border-b-orange-600 | border-bottom-color: var(--color-orange-600); |
| border-b-orange-700 | border-bottom-color: var(--color-orange-700); |
| border-b-orange-800 | border-bottom-color: var(--color-orange-800); |
| border-b-orange-900 | border-bottom-color: var(--color-orange-900); |
| border-b-orange-950 | border-bottom-color: var(--color-orange-950); |
| border-b-amber-50 | border-bottom-color: var(--color-amber-50); |
| border-b-amber-100 | border-bottom-color: var(--color-amber-100); |
| border-b-amber-200 | border-bottom-color: var(--color-amber-200); |
| border-b-amber-300 | border-bottom-color: var(--color-amber-300); |
| border-b-amber-400 | border-bottom-color: var(--color-amber-400); |
| border-b-amber-500 | border-bottom-color: var(--color-amber-500); |
| border-b-amber-600 | border-bottom-color: var(--color-amber-600); |
| border-b-amber-700 | border-bottom-color: var(--color-amber-700); |
| border-b-amber-800 | border-bottom-color: var(--color-amber-800); |
| border-b-amber-900 | border-bottom-color: var(--color-amber-900); |
| border-b-amber-950 | border-bottom-color: var(--color-amber-950); |
| border-b-yellow-50 | border-bottom-color: var(--color-yellow-50); |
| border-b-yellow-100 | border-bottom-color: var(--color-yellow-100); |
| border-b-yellow-200 | border-bottom-color: var(--color-yellow-200); |
| border-b-yellow-300 | border-bottom-color: var(--color-yellow-300); |
| border-b-yellow-400 | border-bottom-color: var(--color-yellow-400); |
| border-b-yellow-500 | border-bottom-color: var(--color-yellow-500); |
| border-b-yellow-600 | border-bottom-color: var(--color-yellow-600); |
| border-b-yellow-700 | border-bottom-color: var(--color-yellow-700); |
| border-b-yellow-800 | border-bottom-color: var(--color-yellow-800); |
| border-b-yellow-900 | border-bottom-color: var(--color-yellow-900); |
| border-b-yellow-950 | border-bottom-color: var(--color-yellow-950); |
| border-b-lime-50 | border-bottom-color: var(--color-lime-50); |
| border-b-lime-100 | border-bottom-color: var(--color-lime-100); |
| border-b-lime-200 | border-bottom-color: var(--color-lime-200); |
| border-b-lime-300 | border-bottom-color: var(--color-lime-300); |
| border-b-lime-400 | border-bottom-color: var(--color-lime-400); |
| border-b-lime-500 | border-bottom-color: var(--color-lime-500); |
| border-b-lime-600 | border-bottom-color: var(--color-lime-600); |
| border-b-lime-700 | border-bottom-color: var(--color-lime-700); |
| border-b-lime-800 | border-bottom-color: var(--color-lime-800); |
| border-b-lime-900 | border-bottom-color: var(--color-lime-900); |
| border-b-lime-950 | border-bottom-color: var(--color-lime-950); |
| border-b-green-50 | border-bottom-color: var(--color-green-50); |
| border-b-green-100 | border-bottom-color: var(--color-green-100); |
| border-b-green-200 | border-bottom-color: var(--color-green-200); |
| border-b-green-300 | border-bottom-color: var(--color-green-300); |
| border-b-green-400 | border-bottom-color: var(--color-green-400); |
| border-b-green-500 | border-bottom-color: var(--color-green-500); |
| border-b-green-600 | border-bottom-color: var(--color-green-600); |
| border-b-green-700 | border-bottom-color: var(--color-green-700); |
| border-b-green-800 | border-bottom-color: var(--color-green-800); |
| border-b-green-900 | border-bottom-color: var(--color-green-900); |
| border-b-green-950 | border-bottom-color: var(--color-green-950); |
| border-b-emerald-50 | border-bottom-color: var(--color-emerald-50); |
| border-b-emerald-100 | border-bottom-color: var(--color-emerald-100); |
| border-b-emerald-200 | border-bottom-color: var(--color-emerald-200); |
| border-b-emerald-300 | border-bottom-color: var(--color-emerald-300); |
| border-b-emerald-400 | border-bottom-color: var(--color-emerald-400); |
| border-b-emerald-500 | border-bottom-color: var(--color-emerald-500); |
| border-b-emerald-600 | border-bottom-color: var(--color-emerald-600); |
| border-b-emerald-700 | border-bottom-color: var(--color-emerald-700); |
| border-b-emerald-800 | border-bottom-color: var(--color-emerald-800); |
| border-b-emerald-900 | border-bottom-color: var(--color-emerald-900); |
| border-b-emerald-950 | border-bottom-color: var(--color-emerald-950); |
| border-b-teal-50 | border-bottom-color: var(--color-teal-50); |
| border-b-teal-100 | border-bottom-color: var(--color-teal-100); |
| border-b-teal-200 | border-bottom-color: var(--color-teal-200); |
| border-b-teal-300 | border-bottom-color: var(--color-teal-300); |
| border-b-teal-400 | border-bottom-color: var(--color-teal-400); |
| border-b-teal-500 | border-bottom-color: var(--color-teal-500); |
| border-b-teal-600 | border-bottom-color: var(--color-teal-600); |
| border-b-teal-700 | border-bottom-color: var(--color-teal-700); |
| border-b-teal-800 | border-bottom-color: var(--color-teal-800); |
| border-b-teal-900 | border-bottom-color: var(--color-teal-900); |
| border-b-teal-950 | border-bottom-color: var(--color-teal-950); |
| border-b-cyan-50 | border-bottom-color: var(--color-cyan-50); |
| border-b-cyan-100 | border-bottom-color: var(--color-cyan-100); |
| border-b-cyan-200 | border-bottom-color: var(--color-cyan-200); |
| border-b-cyan-300 | border-bottom-color: var(--color-cyan-300); |
| border-b-cyan-400 | border-bottom-color: var(--color-cyan-400); |
| border-b-cyan-500 | border-bottom-color: var(--color-cyan-500); |
| border-b-cyan-600 | border-bottom-color: var(--color-cyan-600); |
| border-b-cyan-700 | border-bottom-color: var(--color-cyan-700); |
| border-b-cyan-800 | border-bottom-color: var(--color-cyan-800); |
| border-b-cyan-900 | border-bottom-color: var(--color-cyan-900); |
| border-b-cyan-950 | border-bottom-color: var(--color-cyan-950); |
| border-b-sky-50 | border-bottom-color: var(--color-sky-50); |
| border-b-sky-100 | border-bottom-color: var(--color-sky-100); |
| border-b-sky-200 | border-bottom-color: var(--color-sky-200); |
| border-b-sky-300 | border-bottom-color: var(--color-sky-300); |
| border-b-sky-400 | border-bottom-color: var(--color-sky-400); |
| border-b-sky-500 | border-bottom-color: var(--color-sky-500); |
| border-b-sky-600 | border-bottom-color: var(--color-sky-600); |
| border-b-sky-700 | border-bottom-color: var(--color-sky-700); |
| border-b-sky-800 | border-bottom-color: var(--color-sky-800); |
| border-b-sky-900 | border-bottom-color: var(--color-sky-900); |
| border-b-sky-950 | border-bottom-color: var(--color-sky-950); |
| border-b-blue-50 | border-bottom-color: var(--color-blue-50); |
| border-b-blue-100 | border-bottom-color: var(--color-blue-100); |
| border-b-blue-200 | border-bottom-color: var(--color-blue-200); |
| border-b-blue-300 | border-bottom-color: var(--color-blue-300); |
| border-b-blue-400 | border-bottom-color: var(--color-blue-400); |
| border-b-blue-500 | border-bottom-color: var(--color-blue-500); |
| border-b-blue-600 | border-bottom-color: var(--color-blue-600); |
| border-b-blue-700 | border-bottom-color: var(--color-blue-700); |
| border-b-blue-800 | border-bottom-color: var(--color-blue-800); |
| border-b-blue-900 | border-bottom-color: var(--color-blue-900); |
| border-b-blue-950 | border-bottom-color: var(--color-blue-950); |
| border-b-indigo-50 | border-bottom-color: var(--color-indigo-50); |
| border-b-indigo-100 | border-bottom-color: var(--color-indigo-100); |
| border-b-indigo-200 | border-bottom-color: var(--color-indigo-200); |
| border-b-indigo-300 | border-bottom-color: var(--color-indigo-300); |
| border-b-indigo-400 | border-bottom-color: var(--color-indigo-400); |
| border-b-indigo-500 | border-bottom-color: var(--color-indigo-500); |
| border-b-indigo-600 | border-bottom-color: var(--color-indigo-600); |
| border-b-indigo-700 | border-bottom-color: var(--color-indigo-700); |
| border-b-indigo-800 | border-bottom-color: var(--color-indigo-800); |
| border-b-indigo-900 | border-bottom-color: var(--color-indigo-900); |
| border-b-indigo-950 | border-bottom-color: var(--color-indigo-950); |
| border-b-violet-50 | border-bottom-color: var(--color-violet-50); |
| border-b-violet-100 | border-bottom-color: var(--color-violet-100); |
| border-b-violet-200 | border-bottom-color: var(--color-violet-200); |
| border-b-violet-300 | border-bottom-color: var(--color-violet-300); |
| border-b-violet-400 | border-bottom-color: var(--color-violet-400); |
| border-b-violet-500 | border-bottom-color: var(--color-violet-500); |
| border-b-violet-600 | border-bottom-color: var(--color-violet-600); |
| border-b-violet-700 | border-bottom-color: var(--color-violet-700); |
| border-b-violet-800 | border-bottom-color: var(--color-violet-800); |
| border-b-violet-900 | border-bottom-color: var(--color-violet-900); |
| border-b-violet-950 | border-bottom-color: var(--color-violet-950); |
| border-b-purple-50 | border-bottom-color: var(--color-purple-50); |
| border-b-purple-100 | border-bottom-color: var(--color-purple-100); |
| border-b-purple-200 | border-bottom-color: var(--color-purple-200); |
| border-b-purple-300 | border-bottom-color: var(--color-purple-300); |
| border-b-purple-400 | border-bottom-color: var(--color-purple-400); |
| border-b-purple-500 | border-bottom-color: var(--color-purple-500); |
| border-b-purple-600 | border-bottom-color: var(--color-purple-600); |
| border-b-purple-700 | border-bottom-color: var(--color-purple-700); |
| border-b-purple-800 | border-bottom-color: var(--color-purple-800); |
| border-b-purple-900 | border-bottom-color: var(--color-purple-900); |
| border-b-purple-950 | border-bottom-color: var(--color-purple-950); |
| border-b-fuchsia-50 | border-bottom-color: var(--color-fuchsia-50); |
| border-b-fuchsia-100 | border-bottom-color: var(--color-fuchsia-100); |
| border-b-fuchsia-200 | border-bottom-color: var(--color-fuchsia-200); |
| border-b-fuchsia-300 | border-bottom-color: var(--color-fuchsia-300); |
| border-b-fuchsia-400 | border-bottom-color: var(--color-fuchsia-400); |
| border-b-fuchsia-500 | border-bottom-color: var(--color-fuchsia-500); |
| border-b-fuchsia-600 | border-bottom-color: var(--color-fuchsia-600); |
| border-b-fuchsia-700 | border-bottom-color: var(--color-fuchsia-700); |
| border-b-fuchsia-800 | border-bottom-color: var(--color-fuchsia-800); |
| border-b-fuchsia-900 | border-bottom-color: var(--color-fuchsia-900); |
| border-b-fuchsia-950 | border-bottom-color: var(--color-fuchsia-950); |
| border-b-pink-50 | border-bottom-color: var(--color-pink-50); |
| border-b-pink-100 | border-bottom-color: var(--color-pink-100); |
| border-b-pink-200 | border-bottom-color: var(--color-pink-200); |
| border-b-pink-300 | border-bottom-color: var(--color-pink-300); |
| border-b-pink-400 | border-bottom-color: var(--color-pink-400); |
| border-b-pink-500 | border-bottom-color: var(--color-pink-500); |
| border-b-pink-600 | border-bottom-color: var(--color-pink-600); |
| border-b-pink-700 | border-bottom-color: var(--color-pink-700); |
| border-b-pink-800 | border-bottom-color: var(--color-pink-800); |
| border-b-pink-900 | border-bottom-color: var(--color-pink-900); |
| border-b-pink-950 | border-bottom-color: var(--color-pink-950); |
| border-b-rose-50 | border-bottom-color: var(--color-rose-50); |
| border-b-rose-100 | border-bottom-color: var(--color-rose-100); |
| border-b-rose-200 | border-bottom-color: var(--color-rose-200); |
| border-b-rose-300 | border-bottom-color: var(--color-rose-300); |
| border-b-rose-400 | border-bottom-color: var(--color-rose-400); |
| border-b-rose-500 | border-bottom-color: var(--color-rose-500); |
| border-b-rose-600 | border-bottom-color: var(--color-rose-600); |
| border-b-rose-700 | border-bottom-color: var(--color-rose-700); |
| border-b-rose-800 | border-bottom-color: var(--color-rose-800); |
| border-b-rose-900 | border-bottom-color: var(--color-rose-900); |
| border-b-rose-950 | border-bottom-color: var(--color-rose-950); |
| border-b-slate-50 | border-bottom-color: var(--color-slate-50); |
| border-b-slate-100 | border-bottom-color: var(--color-slate-100); |
| border-b-slate-200 | border-bottom-color: var(--color-slate-200); |
| border-b-slate-300 | border-bottom-color: var(--color-slate-300); |
| border-b-slate-400 | border-bottom-color: var(--color-slate-400); |
| border-b-slate-500 | border-bottom-color: var(--color-slate-500); |
| border-b-slate-600 | border-bottom-color: var(--color-slate-600); |
| border-b-slate-700 | border-bottom-color: var(--color-slate-700); |
| border-b-slate-800 | border-bottom-color: var(--color-slate-800); |
| border-b-slate-900 | border-bottom-color: var(--color-slate-900); |
| border-b-slate-950 | border-bottom-color: var(--color-slate-950); |
| border-b-gray-50 | border-bottom-color: var(--color-gray-50); |
| border-b-gray-100 | border-bottom-color: var(--color-gray-100); |
| border-b-gray-200 | border-bottom-color: var(--color-gray-200); |
| border-b-gray-300 | border-bottom-color: var(--color-gray-300); |
| border-b-gray-400 | border-bottom-color: var(--color-gray-400); |
| border-b-gray-500 | border-bottom-color: var(--color-gray-500); |
| border-b-gray-600 | border-bottom-color: var(--color-gray-600); |
| border-b-gray-700 | border-bottom-color: var(--color-gray-700); |
| border-b-gray-800 | border-bottom-color: var(--color-gray-800); |
| border-b-gray-900 | border-bottom-color: var(--color-gray-900); |
| border-b-gray-950 | border-bottom-color: var(--color-gray-950); |
| border-b-zinc-50 | border-bottom-color: var(--color-zinc-50); |
| border-b-zinc-100 | border-bottom-color: var(--color-zinc-100); |
| border-b-zinc-200 | border-bottom-color: var(--color-zinc-200); |
| border-b-zinc-300 | border-bottom-color: var(--color-zinc-300); |
| border-b-zinc-400 | border-bottom-color: var(--color-zinc-400); |
| border-b-zinc-500 | border-bottom-color: var(--color-zinc-500); |
| border-b-zinc-600 | border-bottom-color: var(--color-zinc-600); |
| border-b-zinc-700 | border-bottom-color: var(--color-zinc-700); |
| border-b-zinc-800 | border-bottom-color: var(--color-zinc-800); |
| border-b-zinc-900 | border-bottom-color: var(--color-zinc-900); |
| border-b-zinc-950 | border-bottom-color: var(--color-zinc-950); |
| border-b-neutral-50 | border-bottom-color: var(--color-neutral-50); |
| border-b-neutral-100 | border-bottom-color: var(--color-neutral-100); |
| border-b-neutral-200 | border-bottom-color: var(--color-neutral-200); |
| border-b-neutral-300 | border-bottom-color: var(--color-neutral-300); |
| border-b-neutral-400 | border-bottom-color: var(--color-neutral-400); |
| border-b-neutral-500 | border-bottom-color: var(--color-neutral-500); |
| border-b-neutral-600 | border-bottom-color: var(--color-neutral-600); |
| border-b-neutral-700 | border-bottom-color: var(--color-neutral-700); |
| border-b-neutral-800 | border-bottom-color: var(--color-neutral-800); |
| border-b-neutral-900 | border-bottom-color: var(--color-neutral-900); |
| border-b-neutral-950 | border-bottom-color: var(--color-neutral-950); |
| border-b-stone-50 | border-bottom-color: var(--color-stone-50); |
| border-b-stone-100 | border-bottom-color: var(--color-stone-100); |
| border-b-stone-200 | border-bottom-color: var(--color-stone-200); |
| border-b-stone-300 | border-bottom-color: var(--color-stone-300); |
| border-b-stone-400 | border-bottom-color: var(--color-stone-400); |
| border-b-stone-500 | border-bottom-color: var(--color-stone-500); |
| border-b-stone-600 | border-bottom-color: var(--color-stone-600); |
| border-b-stone-700 | border-bottom-color: var(--color-stone-700); |
| border-b-stone-800 | border-bottom-color: var(--color-stone-800); |
| border-b-stone-900 | border-bottom-color: var(--color-stone-900); |
| border-b-stone-950 | border-bottom-color: var(--color-stone-950); |
| border-b-(<custom-property>) | border-bottom-color: var(<custom-property>); |
| border-b-[<value>] | border-bottom-color: <value>; |
| border-l-inherit | border-left-color: inherit; |
| border-l-current | border-left-color: currentColor; |
| border-l-transparent | border-left-color: transparent; |
| border-l-black | border-left-color: var(--color-black); /* #000 */ |
| border-l-white | border-left-color: var(--color-white); /* #fff */ |
| border-l-red-50 | border-left-color: var(--color-red-50); |
| border-l-red-100 | border-left-color: var(--color-red-100); |
| border-l-red-200 | border-left-color: var(--color-red-200); |
| border-l-red-300 | border-left-color: var(--color-red-300); |
| border-l-red-400 | border-left-color: var(--color-red-400); |
| border-l-red-500 | border-left-color: var(--color-red-500); |
| border-l-red-600 | border-left-color: var(--color-red-600); |
| border-l-red-700 | border-left-color: var(--color-red-700); |
| border-l-red-800 | border-left-color: var(--color-red-800); |
| border-l-red-900 | border-left-color: var(--color-red-900); |
| border-l-red-950 | border-left-color: var(--color-red-950); |
| border-l-orange-50 | border-left-color: var(--color-orange-50); |
| border-l-orange-100 | border-left-color: var(--color-orange-100); |
| border-l-orange-200 | border-left-color: var(--color-orange-200); |
| border-l-orange-300 | border-left-color: var(--color-orange-300); |
| border-l-orange-400 | border-left-color: var(--color-orange-400); |
| border-l-orange-500 | border-left-color: var(--color-orange-500); |
| border-l-orange-600 | border-left-color: var(--color-orange-600); |
| border-l-orange-700 | border-left-color: var(--color-orange-700); |
| border-l-orange-800 | border-left-color: var(--color-orange-800); |
| border-l-orange-900 | border-left-color: var(--color-orange-900); |
| border-l-orange-950 | border-left-color: var(--color-orange-950); |
| border-l-amber-50 | border-left-color: var(--color-amber-50); |
| border-l-amber-100 | border-left-color: var(--color-amber-100); |
| border-l-amber-200 | border-left-color: var(--color-amber-200); |
| border-l-amber-300 | border-left-color: var(--color-amber-300); |
| border-l-amber-400 | border-left-color: var(--color-amber-400); |
| border-l-amber-500 | border-left-color: var(--color-amber-500); |
| border-l-amber-600 | border-left-color: var(--color-amber-600); |
| border-l-amber-700 | border-left-color: var(--color-amber-700); |
| border-l-amber-800 | border-left-color: var(--color-amber-800); |
| border-l-amber-900 | border-left-color: var(--color-amber-900); |
| border-l-amber-950 | border-left-color: var(--color-amber-950); |
| border-l-yellow-50 | border-left-color: var(--color-yellow-50); |
| border-l-yellow-100 | border-left-color: var(--color-yellow-100); |
| border-l-yellow-200 | border-left-color: var(--color-yellow-200); |
| border-l-yellow-300 | border-left-color: var(--color-yellow-300); |
| border-l-yellow-400 | border-left-color: var(--color-yellow-400); |
| border-l-yellow-500 | border-left-color: var(--color-yellow-500); |
| border-l-yellow-600 | border-left-color: var(--color-yellow-600); |
| border-l-yellow-700 | border-left-color: var(--color-yellow-700); |
| border-l-yellow-800 | border-left-color: var(--color-yellow-800); |
| border-l-yellow-900 | border-left-color: var(--color-yellow-900); |
| border-l-yellow-950 | border-left-color: var(--color-yellow-950); |
| border-l-lime-50 | border-left-color: var(--color-lime-50); |
| border-l-lime-100 | border-left-color: var(--color-lime-100); |
| border-l-lime-200 | border-left-color: var(--color-lime-200); |
| border-l-lime-300 | border-left-color: var(--color-lime-300); |
| border-l-lime-400 | border-left-color: var(--color-lime-400); |
| border-l-lime-500 | border-left-color: var(--color-lime-500); |
| border-l-lime-600 | border-left-color: var(--color-lime-600); |
| border-l-lime-700 | border-left-color: var(--color-lime-700); |
| border-l-lime-800 | border-left-color: var(--color-lime-800); |
| border-l-lime-900 | border-left-color: var(--color-lime-900); |
| border-l-lime-950 | border-left-color: var(--color-lime-950); |
| border-l-green-50 | border-left-color: var(--color-green-50); |
| border-l-green-100 | border-left-color: var(--color-green-100); |
| border-l-green-200 | border-left-color: var(--color-green-200); |
| border-l-green-300 | border-left-color: var(--color-green-300); |
| border-l-green-400 | border-left-color: var(--color-green-400); |
| border-l-green-500 | border-left-color: var(--color-green-500); |
| border-l-green-600 | border-left-color: var(--color-green-600); |
| border-l-green-700 | border-left-color: var(--color-green-700); |
| border-l-green-800 | border-left-color: var(--color-green-800); |
| border-l-green-900 | border-left-color: var(--color-green-900); |
| border-l-green-950 | border-left-color: var(--color-green-950); |
| border-l-emerald-50 | border-left-color: var(--color-emerald-50); |
| border-l-emerald-100 | border-left-color: var(--color-emerald-100); |
| border-l-emerald-200 | border-left-color: var(--color-emerald-200); |
| border-l-emerald-300 | border-left-color: var(--color-emerald-300); |
| border-l-emerald-400 | border-left-color: var(--color-emerald-400); |
| border-l-emerald-500 | border-left-color: var(--color-emerald-500); |
| border-l-emerald-600 | border-left-color: var(--color-emerald-600); |
| border-l-emerald-700 | border-left-color: var(--color-emerald-700); |
| border-l-emerald-800 | border-left-color: var(--color-emerald-800); |
| border-l-emerald-900 | border-left-color: var(--color-emerald-900); |
| border-l-emerald-950 | border-left-color: var(--color-emerald-950); |
| border-l-teal-50 | border-left-color: var(--color-teal-50); |
| border-l-teal-100 | border-left-color: var(--color-teal-100); |
| border-l-teal-200 | border-left-color: var(--color-teal-200); |
| border-l-teal-300 | border-left-color: var(--color-teal-300); |
| border-l-teal-400 | border-left-color: var(--color-teal-400); |
| border-l-teal-500 | border-left-color: var(--color-teal-500); |
| border-l-teal-600 | border-left-color: var(--color-teal-600); |
| border-l-teal-700 | border-left-color: var(--color-teal-700); |
| border-l-teal-800 | border-left-color: var(--color-teal-800); |
| border-l-teal-900 | border-left-color: var(--color-teal-900); |
| border-l-teal-950 | border-left-color: var(--color-teal-950); |
| border-l-cyan-50 | border-left-color: var(--color-cyan-50); |
| border-l-cyan-100 | border-left-color: var(--color-cyan-100); |
| border-l-cyan-200 | border-left-color: var(--color-cyan-200); |
| border-l-cyan-300 | border-left-color: var(--color-cyan-300); |
| border-l-cyan-400 | border-left-color: var(--color-cyan-400); |
| border-l-cyan-500 | border-left-color: var(--color-cyan-500); |
| border-l-cyan-600 | border-left-color: var(--color-cyan-600); |
| border-l-cyan-700 | border-left-color: var(--color-cyan-700); |
| border-l-cyan-800 | border-left-color: var(--color-cyan-800); |
| border-l-cyan-900 | border-left-color: var(--color-cyan-900); |
| border-l-cyan-950 | border-left-color: var(--color-cyan-950); |
| border-l-sky-50 | border-left-color: var(--color-sky-50); |
| border-l-sky-100 | border-left-color: var(--color-sky-100); |
| border-l-sky-200 | border-left-color: var(--color-sky-200); |
| border-l-sky-300 | border-left-color: var(--color-sky-300); |
| border-l-sky-400 | border-left-color: var(--color-sky-400); |
| border-l-sky-500 | border-left-color: var(--color-sky-500); |
| border-l-sky-600 | border-left-color: var(--color-sky-600); |
| border-l-sky-700 | border-left-color: var(--color-sky-700); |
| border-l-sky-800 | border-left-color: var(--color-sky-800); |
| border-l-sky-900 | border-left-color: var(--color-sky-900); |
| border-l-sky-950 | border-left-color: var(--color-sky-950); |
| border-l-blue-50 | border-left-color: var(--color-blue-50); |
| border-l-blue-100 | border-left-color: var(--color-blue-100); |
| border-l-blue-200 | border-left-color: var(--color-blue-200); |
| border-l-blue-300 | border-left-color: var(--color-blue-300); |
| border-l-blue-400 | border-left-color: var(--color-blue-400); |
| border-l-blue-500 | border-left-color: var(--color-blue-500); |
| border-l-blue-600 | border-left-color: var(--color-blue-600); |
| border-l-blue-700 | border-left-color: var(--color-blue-700); |
| border-l-blue-800 | border-left-color: var(--color-blue-800); |
| border-l-blue-900 | border-left-color: var(--color-blue-900); |
| border-l-blue-950 | border-left-color: var(--color-blue-950); |
| border-l-indigo-50 | border-left-color: var(--color-indigo-50); |
| border-l-indigo-100 | border-left-color: var(--color-indigo-100); |
| border-l-indigo-200 | border-left-color: var(--color-indigo-200); |
| border-l-indigo-300 | border-left-color: var(--color-indigo-300); |
| border-l-indigo-400 | border-left-color: var(--color-indigo-400); |
| border-l-indigo-500 | border-left-color: var(--color-indigo-500); |
| border-l-indigo-600 | border-left-color: var(--color-indigo-600); |
| border-l-indigo-700 | border-left-color: var(--color-indigo-700); |
| border-l-indigo-800 | border-left-color: var(--color-indigo-800); |
| border-l-indigo-900 | border-left-color: var(--color-indigo-900); |
| border-l-indigo-950 | border-left-color: var(--color-indigo-950); |
| border-l-violet-50 | border-left-color: var(--color-violet-50); |
| border-l-violet-100 | border-left-color: var(--color-violet-100); |
| border-l-violet-200 | border-left-color: var(--color-violet-200); |
| border-l-violet-300 | border-left-color: var(--color-violet-300); |
| border-l-violet-400 | border-left-color: var(--color-violet-400); |
| border-l-violet-500 | border-left-color: var(--color-violet-500); |
| border-l-violet-600 | border-left-color: var(--color-violet-600); |
| border-l-violet-700 | border-left-color: var(--color-violet-700); |
| border-l-violet-800 | border-left-color: var(--color-violet-800); |
| border-l-violet-900 | border-left-color: var(--color-violet-900); |
| border-l-violet-950 | border-left-color: var(--color-violet-950); |
| border-l-purple-50 | border-left-color: var(--color-purple-50); |
| border-l-purple-100 | border-left-color: var(--color-purple-100); |
| border-l-purple-200 | border-left-color: var(--color-purple-200); |
| border-l-purple-300 | border-left-color: var(--color-purple-300); |
| border-l-purple-400 | border-left-color: var(--color-purple-400); |
| border-l-purple-500 | border-left-color: var(--color-purple-500); |
| border-l-purple-600 | border-left-color: var(--color-purple-600); |
| border-l-purple-700 | border-left-color: var(--color-purple-700); |
| border-l-purple-800 | border-left-color: var(--color-purple-800); |
| border-l-purple-900 | border-left-color: var(--color-purple-900); |
| border-l-purple-950 | border-left-color: var(--color-purple-950); |
| border-l-fuchsia-50 | border-left-color: var(--color-fuchsia-50); |
| border-l-fuchsia-100 | border-left-color: var(--color-fuchsia-100); |
| border-l-fuchsia-200 | border-left-color: var(--color-fuchsia-200); |
| border-l-fuchsia-300 | border-left-color: var(--color-fuchsia-300); |
| border-l-fuchsia-400 | border-left-color: var(--color-fuchsia-400); |
| border-l-fuchsia-500 | border-left-color: var(--color-fuchsia-500); |
| border-l-fuchsia-600 | border-left-color: var(--color-fuchsia-600); |
| border-l-fuchsia-700 | border-left-color: var(--color-fuchsia-700); |
| border-l-fuchsia-800 | border-left-color: var(--color-fuchsia-800); |
| border-l-fuchsia-900 | border-left-color: var(--color-fuchsia-900); |
| border-l-fuchsia-950 | border-left-color: var(--color-fuchsia-950); |
| border-l-pink-50 | border-left-color: var(--color-pink-50); |
| border-l-pink-100 | border-left-color: var(--color-pink-100); |
| border-l-pink-200 | border-left-color: var(--color-pink-200); |
| border-l-pink-300 | border-left-color: var(--color-pink-300); |
| border-l-pink-400 | border-left-color: var(--color-pink-400); |
| border-l-pink-500 | border-left-color: var(--color-pink-500); |
| border-l-pink-600 | border-left-color: var(--color-pink-600); |
| border-l-pink-700 | border-left-color: var(--color-pink-700); |
| border-l-pink-800 | border-left-color: var(--color-pink-800); |
| border-l-pink-900 | border-left-color: var(--color-pink-900); |
| border-l-pink-950 | border-left-color: var(--color-pink-950); |
| border-l-rose-50 | border-left-color: var(--color-rose-50); |
| border-l-rose-100 | border-left-color: var(--color-rose-100); |
| border-l-rose-200 | border-left-color: var(--color-rose-200); |
| border-l-rose-300 | border-left-color: var(--color-rose-300); |
| border-l-rose-400 | border-left-color: var(--color-rose-400); |
| border-l-rose-500 | border-left-color: var(--color-rose-500); |
| border-l-rose-600 | border-left-color: var(--color-rose-600); |
| border-l-rose-700 | border-left-color: var(--color-rose-700); |
| border-l-rose-800 | border-left-color: var(--color-rose-800); |
| border-l-rose-900 | border-left-color: var(--color-rose-900); |
| border-l-rose-950 | border-left-color: var(--color-rose-950); |
| border-l-slate-50 | border-left-color: var(--color-slate-50); |
| border-l-slate-100 | border-left-color: var(--color-slate-100); |
| border-l-slate-200 | border-left-color: var(--color-slate-200); |
| border-l-slate-300 | border-left-color: var(--color-slate-300); |
| border-l-slate-400 | border-left-color: var(--color-slate-400); |
| border-l-slate-500 | border-left-color: var(--color-slate-500); |
| border-l-slate-600 | border-left-color: var(--color-slate-600); |
| border-l-slate-700 | border-left-color: var(--color-slate-700); |
| border-l-slate-800 | border-left-color: var(--color-slate-800); |
| border-l-slate-900 | border-left-color: var(--color-slate-900); |
| border-l-slate-950 | border-left-color: var(--color-slate-950); |
| border-l-gray-50 | border-left-color: var(--color-gray-50); |
| border-l-gray-100 | border-left-color: var(--color-gray-100); |
| border-l-gray-200 | border-left-color: var(--color-gray-200); |
| border-l-gray-300 | border-left-color: var(--color-gray-300); |
| border-l-gray-400 | border-left-color: var(--color-gray-400); |
| border-l-gray-500 | border-left-color: var(--color-gray-500); |
| border-l-gray-600 | border-left-color: var(--color-gray-600); |
| border-l-gray-700 | border-left-color: var(--color-gray-700); |
| border-l-gray-800 | border-left-color: var(--color-gray-800); |
| border-l-gray-900 | border-left-color: var(--color-gray-900); |
| border-l-gray-950 | border-left-color: var(--color-gray-950); |
| border-l-zinc-50 | border-left-color: var(--color-zinc-50); |
| border-l-zinc-100 | border-left-color: var(--color-zinc-100); |
| border-l-zinc-200 | border-left-color: var(--color-zinc-200); |
| border-l-zinc-300 | border-left-color: var(--color-zinc-300); |
| border-l-zinc-400 | border-left-color: var(--color-zinc-400); |
| border-l-zinc-500 | border-left-color: var(--color-zinc-500); |
| border-l-zinc-600 | border-left-color: var(--color-zinc-600); |
| border-l-zinc-700 | border-left-color: var(--color-zinc-700); |
| border-l-zinc-800 | border-left-color: var(--color-zinc-800); |
| border-l-zinc-900 | border-left-color: var(--color-zinc-900); |
| border-l-zinc-950 | border-left-color: var(--color-zinc-950); |
| border-l-neutral-50 | border-left-color: var(--color-neutral-50); |
| border-l-neutral-100 | border-left-color: var(--color-neutral-100); |
| border-l-neutral-200 | border-left-color: var(--color-neutral-200); |
| border-l-neutral-300 | border-left-color: var(--color-neutral-300); |
| border-l-neutral-400 | border-left-color: var(--color-neutral-400); |
| border-l-neutral-500 | border-left-color: var(--color-neutral-500); |
| border-l-neutral-600 | border-left-color: var(--color-neutral-600); |
| border-l-neutral-700 | border-left-color: var(--color-neutral-700); |
| border-l-neutral-800 | border-left-color: var(--color-neutral-800); |
| border-l-neutral-900 | border-left-color: var(--color-neutral-900); |
| border-l-neutral-950 | border-left-color: var(--color-neutral-950); |
| border-l-stone-50 | border-left-color: var(--color-stone-50); |
| border-l-stone-100 | border-left-color: var(--color-stone-100); |
| border-l-stone-200 | border-left-color: var(--color-stone-200); |
| border-l-stone-300 | border-left-color: var(--color-stone-300); |
| border-l-stone-400 | border-left-color: var(--color-stone-400); |
| border-l-stone-500 | border-left-color: var(--color-stone-500); |
| border-l-stone-600 | border-left-color: var(--color-stone-600); |
| border-l-stone-700 | border-left-color: var(--color-stone-700); |
| border-l-stone-800 | border-left-color: var(--color-stone-800); |
| border-l-stone-900 | border-left-color: var(--color-stone-900); |
| border-l-stone-950 | border-left-color: var(--color-stone-950); |
| border-l-(<custom-property>) | border-left-color: var(<custom-property>); |
| border-l-[<value>] | border-left-color: <value>; |
| divide-inherit | & > :not(:last-child) {<br>  border-color: inherit;<br>} |
| divide-current | & > :not(:last-child) {<br>  border-color: currentColor;<br>} |
| divide-transparent | & > :not(:last-child) {<br>  border-color: transparent;<br>} |
| divide-black | & > :not(:last-child) {<br>  border-color: var(--color-black); <br>/* #000 */<br><br>} |
| divide-white | & > :not(:last-child) {<br>  border-color: var(--color-white); <br>/* #fff */<br><br>} |
| divide-red-50 | & > :not(:last-child) {<br>  border-color: var(--color-red-50); <br><br><br>} |
| divide-red-100 | & > :not(:last-child) {<br>  border-color: var(--color-red-100); <br><br><br>} |
| divide-red-200 | & > :not(:last-child) {<br>  border-color: var(--color-red-200); <br><br><br>} |
| divide-red-300 | & > :not(:last-child) {<br>  border-color: var(--color-red-300); <br><br><br>} |
| divide-red-400 | & > :not(:last-child) {<br>  border-color: var(--color-red-400); <br><br><br>} |
| divide-red-500 | & > :not(:last-child) {<br>  border-color: var(--color-red-500); <br><br><br>} |
| divide-red-600 | & > :not(:last-child) {<br>  border-color: var(--color-red-600); <br><br><br>} |
| divide-red-700 | & > :not(:last-child) {<br>  border-color: var(--color-red-700); <br><br><br>} |
| divide-red-800 | & > :not(:last-child) {<br>  border-color: var(--color-red-800); <br><br><br>} |
| divide-red-900 | & > :not(:last-child) {<br>  border-color: var(--color-red-900); <br><br><br>} |
| divide-red-950 | & > :not(:last-child) {<br>  border-color: var(--color-red-950); <br><br><br>} |
| divide-orange-50 | & > :not(:last-child) {<br>  border-color: var(--color-orange-50); <br><br><br>} |
| divide-orange-100 | & > :not(:last-child) {<br>  border-color: var(--color-orange-100); <br><br><br>} |
| divide-orange-200 | & > :not(:last-child) {<br>  border-color: var(--color-orange-200); <br><br><br>} |
| divide-orange-300 | & > :not(:last-child) {<br>  border-color: var(--color-orange-300); <br><br><br>} |
| divide-orange-400 | & > :not(:last-child) {<br>  border-color: var(--color-orange-400); <br><br><br>} |
| divide-orange-500 | & > :not(:last-child) {<br>  border-color: var(--color-orange-500); <br><br><br>} |
| divide-orange-600 | & > :not(:last-child) {<br>  border-color: var(--color-orange-600); <br><br><br>} |
| divide-orange-700 | & > :not(:last-child) {<br>  border-color: var(--color-orange-700); <br><br><br>} |
| divide-orange-800 | & > :not(:last-child) {<br>  border-color: var(--color-orange-800); <br><br><br>} |
| divide-orange-900 | & > :not(:last-child) {<br>  border-color: var(--color-orange-900); <br><br><br>} |
| divide-orange-950 | & > :not(:last-child) {<br>  border-color: var(--color-orange-950); <br><br><br>} |
| divide-amber-50 | & > :not(:last-child) {<br>  border-color: var(--color-amber-50); <br><br><br>} |
| divide-amber-100 | & > :not(:last-child) {<br>  border-color: var(--color-amber-100); <br><br><br>} |
| divide-amber-200 | & > :not(:last-child) {<br>  border-color: var(--color-amber-200); <br><br><br>} |
| divide-amber-300 | & > :not(:last-child) {<br>  border-color: var(--color-amber-300); <br><br><br>} |
| divide-amber-400 | & > :not(:last-child) {<br>  border-color: var(--color-amber-400); <br><br><br>} |
| divide-amber-500 | & > :not(:last-child) {<br>  border-color: var(--color-amber-500); <br><br><br>} |
| divide-amber-600 | & > :not(:last-child) {<br>  border-color: var(--color-amber-600); <br><br><br>} |
| divide-amber-700 | & > :not(:last-child) {<br>  border-color: var(--color-amber-700); <br><br><br>} |
| divide-amber-800 | & > :not(:last-child) {<br>  border-color: var(--color-amber-800); <br><br><br>} |
| divide-amber-900 | & > :not(:last-child) {<br>  border-color: var(--color-amber-900); <br><br><br>} |
| divide-amber-950 | & > :not(:last-child) {<br>  border-color: var(--color-amber-950); <br><br><br>} |
| divide-yellow-50 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-50); <br><br><br>} |
| divide-yellow-100 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-100); <br><br><br>} |
| divide-yellow-200 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-200); <br><br><br>} |
| divide-yellow-300 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-300); <br><br><br>} |
| divide-yellow-400 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-400); <br><br><br>} |
| divide-yellow-500 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-500); <br><br><br>} |
| divide-yellow-600 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-600); <br><br><br>} |
| divide-yellow-700 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-700); <br><br><br>} |
| divide-yellow-800 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-800); <br><br><br>} |
| divide-yellow-900 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-900); <br><br><br>} |
| divide-yellow-950 | & > :not(:last-child) {<br>  border-color: var(--color-yellow-950); <br><br><br>} |
| divide-lime-50 | & > :not(:last-child) {<br>  border-color: var(--color-lime-50); <br><br><br>} |
| divide-lime-100 | & > :not(:last-child) {<br>  border-color: var(--color-lime-100); <br><br><br>} |
| divide-lime-200 | & > :not(:last-child) {<br>  border-color: var(--color-lime-200); <br><br><br>} |
| divide-lime-300 | & > :not(:last-child) {<br>  border-color: var(--color-lime-300); <br><br><br>} |
| divide-lime-400 | & > :not(:last-child) {<br>  border-color: var(--color-lime-400); <br><br><br>} |
| divide-lime-500 | & > :not(:last-child) {<br>  border-color: var(--color-lime-500); <br><br><br>} |
| divide-lime-600 | & > :not(:last-child) {<br>  border-color: var(--color-lime-600); <br><br><br>} |
| divide-lime-700 | & > :not(:last-child) {<br>  border-color: var(--color-lime-700); <br><br><br>} |
| divide-lime-800 | & > :not(:last-child) {<br>  border-color: var(--color-lime-800); <br><br><br>} |
| divide-lime-900 | & > :not(:last-child) {<br>  border-color: var(--color-lime-900); <br><br><br>} |
| divide-lime-950 | & > :not(:last-child) {<br>  border-color: var(--color-lime-950); <br><br><br>} |
| divide-green-50 | & > :not(:last-child) {<br>  border-color: var(--color-green-50); <br><br><br>} |
| divide-green-100 | & > :not(:last-child) {<br>  border-color: var(--color-green-100); <br><br><br>} |
| divide-green-200 | & > :not(:last-child) {<br>  border-color: var(--color-green-200); <br><br><br>} |
| divide-green-300 | & > :not(:last-child) {<br>  border-color: var(--color-green-300); <br><br><br>} |
| divide-green-400 | & > :not(:last-child) {<br>  border-color: var(--color-green-400); <br><br><br>} |
| divide-green-500 | & > :not(:last-child) {<br>  border-color: var(--color-green-500); <br><br><br>} |
| divide-green-600 | & > :not(:last-child) {<br>  border-color: var(--color-green-600); <br><br><br>} |
| divide-green-700 | & > :not(:last-child) {<br>  border-color: var(--color-green-700); <br><br><br>} |
| divide-green-800 | & > :not(:last-child) {<br>  border-color: var(--color-green-800); <br><br><br>} |
| divide-green-900 | & > :not(:last-child) {<br>  border-color: var(--color-green-900); <br><br><br>} |
| divide-green-950 | & > :not(:last-child) {<br>  border-color: var(--color-green-950); <br><br><br>} |
| divide-emerald-50 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-50); <br><br><br>} |
| divide-emerald-100 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-100); <br><br><br>} |
| divide-emerald-200 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-200); <br><br><br>} |
| divide-emerald-300 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-300); <br><br><br>} |
| divide-emerald-400 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-400); <br><br><br>} |
| divide-emerald-500 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-500); <br><br><br>} |
| divide-emerald-600 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-600); <br><br><br>} |
| divide-emerald-700 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-700); <br><br><br>} |
| divide-emerald-800 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-800); <br><br><br>} |
| divide-emerald-900 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-900); <br><br><br>} |
| divide-emerald-950 | & > :not(:last-child) {<br>  border-color: var(--color-emerald-950); <br><br><br>} |
| divide-teal-50 | & > :not(:last-child) {<br>  border-color: var(--color-teal-50); <br><br><br>} |
| divide-teal-100 | & > :not(:last-child) {<br>  border-color: var(--color-teal-100); <br><br><br>} |
| divide-teal-200 | & > :not(:last-child) {<br>  border-color: var(--color-teal-200); <br><br><br>} |
| divide-teal-300 | & > :not(:last-child) {<br>  border-color: var(--color-teal-300); <br><br><br>} |
| divide-teal-400 | & > :not(:last-child) {<br>  border-color: var(--color-teal-400); <br><br><br>} |
| divide-teal-500 | & > :not(:last-child) {<br>  border-color: var(--color-teal-500); <br><br><br>} |
| divide-teal-600 | & > :not(:last-child) {<br>  border-color: var(--color-teal-600); <br><br><br>} |
| divide-teal-700 | & > :not(:last-child) {<br>  border-color: var(--color-teal-700); <br><br><br>} |
| divide-teal-800 | & > :not(:last-child) {<br>  border-color: var(--color-teal-800); <br><br><br>} |
| divide-teal-900 | & > :not(:last-child) {<br>  border-color: var(--color-teal-900); <br><br><br>} |
| divide-teal-950 | & > :not(:last-child) {<br>  border-color: var(--color-teal-950); <br><br><br>} |
| divide-cyan-50 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-50); <br><br><br>} |
| divide-cyan-100 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-100); <br><br><br>} |
| divide-cyan-200 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-200); <br><br><br>} |
| divide-cyan-300 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-300); <br><br><br>} |
| divide-cyan-400 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-400); <br><br><br>} |
| divide-cyan-500 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-500); <br><br><br>} |
| divide-cyan-600 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-600); <br><br><br>} |
| divide-cyan-700 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-700); <br><br><br>} |
| divide-cyan-800 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-800); <br><br><br>} |
| divide-cyan-900 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-900); <br><br><br>} |
| divide-cyan-950 | & > :not(:last-child) {<br>  border-color: var(--color-cyan-950); <br><br><br>} |
| divide-sky-50 | & > :not(:last-child) {<br>  border-color: var(--color-sky-50); <br><br><br>} |
| divide-sky-100 | & > :not(:last-child) {<br>  border-color: var(--color-sky-100); <br><br><br>} |
| divide-sky-200 | & > :not(:last-child) {<br>  border-color: var(--color-sky-200); <br><br><br>} |
| divide-sky-300 | & > :not(:last-child) {<br>  border-color: var(--color-sky-300); <br><br><br>} |
| divide-sky-400 | & > :not(:last-child) {<br>  border-color: var(--color-sky-400); <br><br><br>} |
| divide-sky-500 | & > :not(:last-child) {<br>  border-color: var(--color-sky-500); <br><br><br>} |
| divide-sky-600 | & > :not(:last-child) {<br>  border-color: var(--color-sky-600); <br><br><br>} |
| divide-sky-700 | & > :not(:last-child) {<br>  border-color: var(--color-sky-700); <br><br><br>} |
| divide-sky-800 | & > :not(:last-child) {<br>  border-color: var(--color-sky-800); <br><br><br>} |
| divide-sky-900 | & > :not(:last-child) {<br>  border-color: var(--color-sky-900); <br><br><br>} |
| divide-sky-950 | & > :not(:last-child) {<br>  border-color: var(--color-sky-950); <br><br><br>} |
| divide-blue-50 | & > :not(:last-child) {<br>  border-color: var(--color-blue-50); <br><br><br>} |
| divide-blue-100 | & > :not(:last-child) {<br>  border-color: var(--color-blue-100); <br><br><br>} |
| divide-blue-200 | & > :not(:last-child) {<br>  border-color: var(--color-blue-200); <br><br><br>} |
| divide-blue-300 | & > :not(:last-child) {<br>  border-color: var(--color-blue-300); <br><br><br>} |
| divide-blue-400 | & > :not(:last-child) {<br>  border-color: var(--color-blue-400); <br><br><br>} |
| divide-blue-500 | & > :not(:last-child) {<br>  border-color: var(--color-blue-500); <br><br><br>} |
| divide-blue-600 | & > :not(:last-child) {<br>  border-color: var(--color-blue-600); <br><br><br>} |
| divide-blue-700 | & > :not(:last-child) {<br>  border-color: var(--color-blue-700); <br><br><br>} |
| divide-blue-800 | & > :not(:last-child) {<br>  border-color: var(--color-blue-800); <br><br><br>} |
| divide-blue-900 | & > :not(:last-child) {<br>  border-color: var(--color-blue-900); <br><br><br>} |
| divide-blue-950 | & > :not(:last-child) {<br>  border-color: var(--color-blue-950); <br><br><br>} |
| divide-indigo-50 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-50); <br><br><br>} |
| divide-indigo-100 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-100); <br><br><br>} |
| divide-indigo-200 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-200); <br><br><br>} |
| divide-indigo-300 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-300); <br><br><br>} |
| divide-indigo-400 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-400); <br><br><br>} |
| divide-indigo-500 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-500); <br><br><br>} |
| divide-indigo-600 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-600); <br><br><br>} |
| divide-indigo-700 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-700); <br><br><br>} |
| divide-indigo-800 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-800); <br><br><br>} |
| divide-indigo-900 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-900); <br><br><br>} |
| divide-indigo-950 | & > :not(:last-child) {<br>  border-color: var(--color-indigo-950); <br><br><br>} |
| divide-violet-50 | & > :not(:last-child) {<br>  border-color: var(--color-violet-50); <br><br><br>} |
| divide-violet-100 | & > :not(:last-child) {<br>  border-color: var(--color-violet-100); <br><br><br>} |
| divide-violet-200 | & > :not(:last-child) {<br>  border-color: var(--color-violet-200); <br><br><br>} |
| divide-violet-300 | & > :not(:last-child) {<br>  border-color: var(--color-violet-300); <br><br><br>} |
| divide-violet-400 | & > :not(:last-child) {<br>  border-color: var(--color-violet-400); <br><br><br>} |
| divide-violet-500 | & > :not(:last-child) {<br>  border-color: var(--color-violet-500); <br><br><br>} |
| divide-violet-600 | & > :not(:last-child) {<br>  border-color: var(--color-violet-600); <br><br><br>} |
| divide-violet-700 | & > :not(:last-child) {<br>  border-color: var(--color-violet-700); <br><br><br>} |
| divide-violet-800 | & > :not(:last-child) {<br>  border-color: var(--color-violet-800); <br><br><br>} |
| divide-violet-900 | & > :not(:last-child) {<br>  border-color: var(--color-violet-900); <br><br><br>} |
| divide-violet-950 | & > :not(:last-child) {<br>  border-color: var(--color-violet-950); <br><br><br>} |
| divide-purple-50 | & > :not(:last-child) {<br>  border-color: var(--color-purple-50); <br><br><br>} |
| divide-purple-100 | & > :not(:last-child) {<br>  border-color: var(--color-purple-100); <br><br><br>} |
| divide-purple-200 | & > :not(:last-child) {<br>  border-color: var(--color-purple-200); <br><br><br>} |
| divide-purple-300 | & > :not(:last-child) {<br>  border-color: var(--color-purple-300); <br><br><br>} |
| divide-purple-400 | & > :not(:last-child) {<br>  border-color: var(--color-purple-400); <br><br><br>} |
| divide-purple-500 | & > :not(:last-child) {<br>  border-color: var(--color-purple-500); <br><br><br>} |
| divide-purple-600 | & > :not(:last-child) {<br>  border-color: var(--color-purple-600); <br><br><br>} |
| divide-purple-700 | & > :not(:last-child) {<br>  border-color: var(--color-purple-700); <br><br><br>} |
| divide-purple-800 | & > :not(:last-child) {<br>  border-color: var(--color-purple-800); <br><br><br>} |
| divide-purple-900 | & > :not(:last-child) {<br>  border-color: var(--color-purple-900); <br><br><br>} |
| divide-purple-950 | & > :not(:last-child) {<br>  border-color: var(--color-purple-950); <br><br><br>} |
| divide-fuchsia-50 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-50); <br><br><br>} |
| divide-fuchsia-100 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-100); <br><br><br>} |
| divide-fuchsia-200 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-200); <br><br><br>} |
| divide-fuchsia-300 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-300); <br><br><br>} |
| divide-fuchsia-400 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-400); <br><br><br>} |
| divide-fuchsia-500 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-500); <br><br><br>} |
| divide-fuchsia-600 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-600); <br><br><br>} |
| divide-fuchsia-700 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-700); <br><br><br>} |
| divide-fuchsia-800 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-800); <br><br><br>} |
| divide-fuchsia-900 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-900); <br><br><br>} |
| divide-fuchsia-950 | & > :not(:last-child) {<br>  border-color: var(--color-fuchsia-950); <br><br><br>} |
| divide-pink-50 | & > :not(:last-child) {<br>  border-color: var(--color-pink-50); <br><br><br>} |
| divide-pink-100 | & > :not(:last-child) {<br>  border-color: var(--color-pink-100); <br><br><br>} |
| divide-pink-200 | & > :not(:last-child) {<br>  border-color: var(--color-pink-200); <br><br><br>} |
| divide-pink-300 | & > :not(:last-child) {<br>  border-color: var(--color-pink-300); <br><br><br>} |
| divide-pink-400 | & > :not(:last-child) {<br>  border-color: var(--color-pink-400); <br><br><br>} |
| divide-pink-500 | & > :not(:last-child) {<br>  border-color: var(--color-pink-500); <br><br><br>} |
| divide-pink-600 | & > :not(:last-child) {<br>  border-color: var(--color-pink-600); <br><br><br>} |
| divide-pink-700 | & > :not(:last-child) {<br>  border-color: var(--color-pink-700); <br><br><br>} |
| divide-pink-800 | & > :not(:last-child) {<br>  border-color: var(--color-pink-800); <br><br><br>} |
| divide-pink-900 | & > :not(:last-child) {<br>  border-color: var(--color-pink-900); <br><br><br>} |
| divide-pink-950 | & > :not(:last-child) {<br>  border-color: var(--color-pink-950); <br><br><br>} |
| divide-rose-50 | & > :not(:last-child) {<br>  border-color: var(--color-rose-50); <br><br><br>} |
| divide-rose-100 | & > :not(:last-child) {<br>  border-color: var(--color-rose-100); <br><br><br>} |
| divide-rose-200 | & > :not(:last-child) {<br>  border-color: var(--color-rose-200); <br><br><br>} |
| divide-rose-300 | & > :not(:last-child) {<br>  border-color: var(--color-rose-300); <br><br><br>} |
| divide-rose-400 | & > :not(:last-child) {<br>  border-color: var(--color-rose-400); <br><br><br>} |
| divide-rose-500 | & > :not(:last-child) {<br>  border-color: var(--color-rose-500); <br><br><br>} |
| divide-rose-600 | & > :not(:last-child) {<br>  border-color: var(--color-rose-600); <br><br><br>} |
| divide-rose-700 | & > :not(:last-child) {<br>  border-color: var(--color-rose-700); <br><br><br>} |
| divide-rose-800 | & > :not(:last-child) {<br>  border-color: var(--color-rose-800); <br><br><br>} |
| divide-rose-900 | & > :not(:last-child) {<br>  border-color: var(--color-rose-900); <br><br><br>} |
| divide-rose-950 | & > :not(:last-child) {<br>  border-color: var(--color-rose-950); <br><br><br>} |
| divide-slate-50 | & > :not(:last-child) {<br>  border-color: var(--color-slate-50); <br><br><br>} |
| divide-slate-100 | & > :not(:last-child) {<br>  border-color: var(--color-slate-100); <br><br><br>} |
| divide-slate-200 | & > :not(:last-child) {<br>  border-color: var(--color-slate-200); <br><br><br>} |
| divide-slate-300 | & > :not(:last-child) {<br>  border-color: var(--color-slate-300); <br><br><br>} |
| divide-slate-400 | & > :not(:last-child) {<br>  border-color: var(--color-slate-400); <br><br><br>} |
| divide-slate-500 | & > :not(:last-child) {<br>  border-color: var(--color-slate-500); <br><br><br>} |
| divide-slate-600 | & > :not(:last-child) {<br>  border-color: var(--color-slate-600); <br><br><br>} |
| divide-slate-700 | & > :not(:last-child) {<br>  border-color: var(--color-slate-700); <br><br><br>} |
| divide-slate-800 | & > :not(:last-child) {<br>  border-color: var(--color-slate-800); <br><br><br>} |
| divide-slate-900 | & > :not(:last-child) {<br>  border-color: var(--color-slate-900); <br><br><br>} |
| divide-slate-950 | & > :not(:last-child) {<br>  border-color: var(--color-slate-950); <br><br><br>} |
| divide-gray-50 | & > :not(:last-child) {<br>  border-color: var(--color-gray-50); <br><br><br>} |
| divide-gray-100 | & > :not(:last-child) {<br>  border-color: var(--color-gray-100); <br><br><br>} |
| divide-gray-200 | & > :not(:last-child) {<br>  border-color: var(--color-gray-200); <br><br><br>} |
| divide-gray-300 | & > :not(:last-child) {<br>  border-color: var(--color-gray-300); <br><br><br>} |
| divide-gray-400 | & > :not(:last-child) {<br>  border-color: var(--color-gray-400); <br><br><br>} |
| divide-gray-500 | & > :not(:last-child) {<br>  border-color: var(--color-gray-500); <br><br><br>} |
| divide-gray-600 | & > :not(:last-child) {<br>  border-color: var(--color-gray-600); <br><br><br>} |
| divide-gray-700 | & > :not(:last-child) {<br>  border-color: var(--color-gray-700); <br><br><br>} |
| divide-gray-800 | & > :not(:last-child) {<br>  border-color: var(--color-gray-800); <br><br><br>} |
| divide-gray-900 | & > :not(:last-child) {<br>  border-color: var(--color-gray-900); <br><br><br>} |
| divide-gray-950 | & > :not(:last-child) {<br>  border-color: var(--color-gray-950); <br><br><br>} |
| divide-zinc-50 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-50); <br><br><br>} |
| divide-zinc-100 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-100); <br><br><br>} |
| divide-zinc-200 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-200); <br><br><br>} |
| divide-zinc-300 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-300); <br><br><br>} |
| divide-zinc-400 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-400); <br><br><br>} |
| divide-zinc-500 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-500); <br><br><br>} |
| divide-zinc-600 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-600); <br><br><br>} |
| divide-zinc-700 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-700); <br><br><br>} |
| divide-zinc-800 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-800); <br><br><br>} |
| divide-zinc-900 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-900); <br><br><br>} |
| divide-zinc-950 | & > :not(:last-child) {<br>  border-color: var(--color-zinc-950); <br><br><br>} |
| divide-neutral-50 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-50); <br><br><br>} |
| divide-neutral-100 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-100); <br><br><br>} |
| divide-neutral-200 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-200); <br><br><br>} |
| divide-neutral-300 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-300); <br><br><br>} |
| divide-neutral-400 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-400); <br><br><br>} |
| divide-neutral-500 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-500); <br><br><br>} |
| divide-neutral-600 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-600); <br><br><br>} |
| divide-neutral-700 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-700); <br><br><br>} |
| divide-neutral-800 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-800); <br><br><br>} |
| divide-neutral-900 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-900); <br><br><br>} |
| divide-neutral-950 | & > :not(:last-child) {<br>  border-color: var(--color-neutral-950); <br><br><br>} |
| divide-stone-50 | & > :not(:last-child) {<br>  border-color: var(--color-stone-50); <br><br><br>} |
| divide-stone-100 | & > :not(:last-child) {<br>  border-color: var(--color-stone-100); <br><br><br>} |
| divide-stone-200 | & > :not(:last-child) {<br>  border-color: var(--color-stone-200); <br><br><br>} |
| divide-stone-300 | & > :not(:last-child) {<br>  border-color: var(--color-stone-300); <br><br><br>} |
| divide-stone-400 | & > :not(:last-child) {<br>  border-color: var(--color-stone-400); <br><br><br>} |
| divide-stone-500 | & > :not(:last-child) {<br>  border-color: var(--color-stone-500); <br><br><br>} |
| divide-stone-600 | & > :not(:last-child) {<br>  border-color: var(--color-stone-600); <br><br><br>} |
| divide-stone-700 | & > :not(:last-child) {<br>  border-color: var(--color-stone-700); <br><br><br>} |
| divide-stone-800 | & > :not(:last-child) {<br>  border-color: var(--color-stone-800); <br><br><br>} |
| divide-stone-900 | & > :not(:last-child) {<br>  border-color: var(--color-stone-900); <br><br><br>} |
| divide-stone-950 | & > :not(:last-child) {<br>  border-color: var(--color-stone-950); <br><br><br>} |
| divide-(<custom-property>) | & > :not(:last-child) {<br>  border-color: var(<br><custom-property><br>);<br>} |
| divide-[<value>] | & > :not(:last-child) {<br>  border-color: <br><value><br>;<br>} |

[Documentation](https://tailwindcss.com/docs/border-color)

---

## border-style

Utilities for controlling the style of an element's borders.

### Classes

| Class | Styles |
| --- | --- |
| border-solid | border-style: solid; |
| border-dashed | border-style: dashed; |
| border-dotted | border-style: dotted; |
| border-double | border-style: double; |
| border-hidden | border-style: hidden; |
| border-none | border-style: none; |
| divide-solid | & > :not(:last-child) {<br>  border-style: solid;<br>} |
| divide-dashed | & > :not(:last-child) {<br>  border-style: dashed;<br>} |
| divide-dotted | & > :not(:last-child) {<br>  border-style: dotted;<br>} |
| divide-double | & > :not(:last-child) {<br>  border-style: double;<br>} |
| divide-hidden | & > :not(:last-child) {<br>  border-style: hidden;<br>} |
| divide-none | & > :not(:last-child) {<br>  border-style: none;<br>} |

[Documentation](https://tailwindcss.com/docs/border-style)

---

## outline-width

Utilities for controlling the width of an element's outline.

### Classes

| Class | Styles |
| --- | --- |
| outline | outline-width: 1px; |
| outline-<number> | outline-width: <number>px; |
| outline-(length:<custom-property>) | outline-width: var(<custom-property>); |
| outline-[<value>] | outline-width: <value>; |

[Documentation](https://tailwindcss.com/docs/outline-width)

---

## outline-color

Utilities for controlling the color of an element's outline.

### Classes

| Class | Styles |
| --- | --- |
| outline-inherit | outline-color: inherit; |
| outline-current | outline-color: currentColor; |
| outline-transparent | outline-color: transparent; |
| outline-black | outline-color: var(--color-black); /* #000 */ |
| outline-white | outline-color: var(--color-white); /* #fff */ |
| outline-red-50 | outline-color: var(--color-red-50); |
| outline-red-100 | outline-color: var(--color-red-100); |
| outline-red-200 | outline-color: var(--color-red-200); |
| outline-red-300 | outline-color: var(--color-red-300); |
| outline-red-400 | outline-color: var(--color-red-400); |
| outline-red-500 | outline-color: var(--color-red-500); |
| outline-red-600 | outline-color: var(--color-red-600); |
| outline-red-700 | outline-color: var(--color-red-700); |
| outline-red-800 | outline-color: var(--color-red-800); |
| outline-red-900 | outline-color: var(--color-red-900); |
| outline-red-950 | outline-color: var(--color-red-950); |
| outline-orange-50 | outline-color: var(--color-orange-50); |
| outline-orange-100 | outline-color: var(--color-orange-100); |
| outline-orange-200 | outline-color: var(--color-orange-200); |
| outline-orange-300 | outline-color: var(--color-orange-300); |
| outline-orange-400 | outline-color: var(--color-orange-400); |
| outline-orange-500 | outline-color: var(--color-orange-500); |
| outline-orange-600 | outline-color: var(--color-orange-600); |
| outline-orange-700 | outline-color: var(--color-orange-700); |
| outline-orange-800 | outline-color: var(--color-orange-800); |
| outline-orange-900 | outline-color: var(--color-orange-900); |
| outline-orange-950 | outline-color: var(--color-orange-950); |
| outline-amber-50 | outline-color: var(--color-amber-50); |
| outline-amber-100 | outline-color: var(--color-amber-100); |
| outline-amber-200 | outline-color: var(--color-amber-200); |
| outline-amber-300 | outline-color: var(--color-amber-300); |
| outline-amber-400 | outline-color: var(--color-amber-400); |
| outline-amber-500 | outline-color: var(--color-amber-500); |
| outline-amber-600 | outline-color: var(--color-amber-600); |
| outline-amber-700 | outline-color: var(--color-amber-700); |
| outline-amber-800 | outline-color: var(--color-amber-800); |
| outline-amber-900 | outline-color: var(--color-amber-900); |
| outline-amber-950 | outline-color: var(--color-amber-950); |
| outline-yellow-50 | outline-color: var(--color-yellow-50); |
| outline-yellow-100 | outline-color: var(--color-yellow-100); |
| outline-yellow-200 | outline-color: var(--color-yellow-200); |
| outline-yellow-300 | outline-color: var(--color-yellow-300); |
| outline-yellow-400 | outline-color: var(--color-yellow-400); |
| outline-yellow-500 | outline-color: var(--color-yellow-500); |
| outline-yellow-600 | outline-color: var(--color-yellow-600); |
| outline-yellow-700 | outline-color: var(--color-yellow-700); |
| outline-yellow-800 | outline-color: var(--color-yellow-800); |
| outline-yellow-900 | outline-color: var(--color-yellow-900); |
| outline-yellow-950 | outline-color: var(--color-yellow-950); |
| outline-lime-50 | outline-color: var(--color-lime-50); |
| outline-lime-100 | outline-color: var(--color-lime-100); |
| outline-lime-200 | outline-color: var(--color-lime-200); |
| outline-lime-300 | outline-color: var(--color-lime-300); |
| outline-lime-400 | outline-color: var(--color-lime-400); |
| outline-lime-500 | outline-color: var(--color-lime-500); |
| outline-lime-600 | outline-color: var(--color-lime-600); |
| outline-lime-700 | outline-color: var(--color-lime-700); |
| outline-lime-800 | outline-color: var(--color-lime-800); |
| outline-lime-900 | outline-color: var(--color-lime-900); |
| outline-lime-950 | outline-color: var(--color-lime-950); |
| outline-green-50 | outline-color: var(--color-green-50); |
| outline-green-100 | outline-color: var(--color-green-100); |
| outline-green-200 | outline-color: var(--color-green-200); |
| outline-green-300 | outline-color: var(--color-green-300); |
| outline-green-400 | outline-color: var(--color-green-400); |
| outline-green-500 | outline-color: var(--color-green-500); |
| outline-green-600 | outline-color: var(--color-green-600); |
| outline-green-700 | outline-color: var(--color-green-700); |
| outline-green-800 | outline-color: var(--color-green-800); |
| outline-green-900 | outline-color: var(--color-green-900); |
| outline-green-950 | outline-color: var(--color-green-950); |
| outline-emerald-50 | outline-color: var(--color-emerald-50); |
| outline-emerald-100 | outline-color: var(--color-emerald-100); |
| outline-emerald-200 | outline-color: var(--color-emerald-200); |
| outline-emerald-300 | outline-color: var(--color-emerald-300); |
| outline-emerald-400 | outline-color: var(--color-emerald-400); |
| outline-emerald-500 | outline-color: var(--color-emerald-500); |
| outline-emerald-600 | outline-color: var(--color-emerald-600); |
| outline-emerald-700 | outline-color: var(--color-emerald-700); |
| outline-emerald-800 | outline-color: var(--color-emerald-800); |
| outline-emerald-900 | outline-color: var(--color-emerald-900); |
| outline-emerald-950 | outline-color: var(--color-emerald-950); |
| outline-teal-50 | outline-color: var(--color-teal-50); |
| outline-teal-100 | outline-color: var(--color-teal-100); |
| outline-teal-200 | outline-color: var(--color-teal-200); |
| outline-teal-300 | outline-color: var(--color-teal-300); |
| outline-teal-400 | outline-color: var(--color-teal-400); |
| outline-teal-500 | outline-color: var(--color-teal-500); |
| outline-teal-600 | outline-color: var(--color-teal-600); |
| outline-teal-700 | outline-color: var(--color-teal-700); |
| outline-teal-800 | outline-color: var(--color-teal-800); |
| outline-teal-900 | outline-color: var(--color-teal-900); |
| outline-teal-950 | outline-color: var(--color-teal-950); |
| outline-cyan-50 | outline-color: var(--color-cyan-50); |
| outline-cyan-100 | outline-color: var(--color-cyan-100); |
| outline-cyan-200 | outline-color: var(--color-cyan-200); |
| outline-cyan-300 | outline-color: var(--color-cyan-300); |
| outline-cyan-400 | outline-color: var(--color-cyan-400); |
| outline-cyan-500 | outline-color: var(--color-cyan-500); |
| outline-cyan-600 | outline-color: var(--color-cyan-600); |
| outline-cyan-700 | outline-color: var(--color-cyan-700); |
| outline-cyan-800 | outline-color: var(--color-cyan-800); |
| outline-cyan-900 | outline-color: var(--color-cyan-900); |
| outline-cyan-950 | outline-color: var(--color-cyan-950); |
| outline-sky-50 | outline-color: var(--color-sky-50); |
| outline-sky-100 | outline-color: var(--color-sky-100); |
| outline-sky-200 | outline-color: var(--color-sky-200); |
| outline-sky-300 | outline-color: var(--color-sky-300); |
| outline-sky-400 | outline-color: var(--color-sky-400); |
| outline-sky-500 | outline-color: var(--color-sky-500); |
| outline-sky-600 | outline-color: var(--color-sky-600); |
| outline-sky-700 | outline-color: var(--color-sky-700); |
| outline-sky-800 | outline-color: var(--color-sky-800); |
| outline-sky-900 | outline-color: var(--color-sky-900); |
| outline-sky-950 | outline-color: var(--color-sky-950); |
| outline-blue-50 | outline-color: var(--color-blue-50); |
| outline-blue-100 | outline-color: var(--color-blue-100); |
| outline-blue-200 | outline-color: var(--color-blue-200); |
| outline-blue-300 | outline-color: var(--color-blue-300); |
| outline-blue-400 | outline-color: var(--color-blue-400); |
| outline-blue-500 | outline-color: var(--color-blue-500); |
| outline-blue-600 | outline-color: var(--color-blue-600); |
| outline-blue-700 | outline-color: var(--color-blue-700); |
| outline-blue-800 | outline-color: var(--color-blue-800); |
| outline-blue-900 | outline-color: var(--color-blue-900); |
| outline-blue-950 | outline-color: var(--color-blue-950); |
| outline-indigo-50 | outline-color: var(--color-indigo-50); |
| outline-indigo-100 | outline-color: var(--color-indigo-100); |
| outline-indigo-200 | outline-color: var(--color-indigo-200); |
| outline-indigo-300 | outline-color: var(--color-indigo-300); |
| outline-indigo-400 | outline-color: var(--color-indigo-400); |
| outline-indigo-500 | outline-color: var(--color-indigo-500); |
| outline-indigo-600 | outline-color: var(--color-indigo-600); |
| outline-indigo-700 | outline-color: var(--color-indigo-700); |
| outline-indigo-800 | outline-color: var(--color-indigo-800); |
| outline-indigo-900 | outline-color: var(--color-indigo-900); |
| outline-indigo-950 | outline-color: var(--color-indigo-950); |
| outline-violet-50 | outline-color: var(--color-violet-50); |
| outline-violet-100 | outline-color: var(--color-violet-100); |
| outline-violet-200 | outline-color: var(--color-violet-200); |
| outline-violet-300 | outline-color: var(--color-violet-300); |
| outline-violet-400 | outline-color: var(--color-violet-400); |
| outline-violet-500 | outline-color: var(--color-violet-500); |
| outline-violet-600 | outline-color: var(--color-violet-600); |
| outline-violet-700 | outline-color: var(--color-violet-700); |
| outline-violet-800 | outline-color: var(--color-violet-800); |
| outline-violet-900 | outline-color: var(--color-violet-900); |
| outline-violet-950 | outline-color: var(--color-violet-950); |
| outline-purple-50 | outline-color: var(--color-purple-50); |
| outline-purple-100 | outline-color: var(--color-purple-100); |
| outline-purple-200 | outline-color: var(--color-purple-200); |
| outline-purple-300 | outline-color: var(--color-purple-300); |
| outline-purple-400 | outline-color: var(--color-purple-400); |
| outline-purple-500 | outline-color: var(--color-purple-500); |
| outline-purple-600 | outline-color: var(--color-purple-600); |
| outline-purple-700 | outline-color: var(--color-purple-700); |
| outline-purple-800 | outline-color: var(--color-purple-800); |
| outline-purple-900 | outline-color: var(--color-purple-900); |
| outline-purple-950 | outline-color: var(--color-purple-950); |
| outline-fuchsia-50 | outline-color: var(--color-fuchsia-50); |
| outline-fuchsia-100 | outline-color: var(--color-fuchsia-100); |
| outline-fuchsia-200 | outline-color: var(--color-fuchsia-200); |
| outline-fuchsia-300 | outline-color: var(--color-fuchsia-300); |
| outline-fuchsia-400 | outline-color: var(--color-fuchsia-400); |
| outline-fuchsia-500 | outline-color: var(--color-fuchsia-500); |
| outline-fuchsia-600 | outline-color: var(--color-fuchsia-600); |
| outline-fuchsia-700 | outline-color: var(--color-fuchsia-700); |
| outline-fuchsia-800 | outline-color: var(--color-fuchsia-800); |
| outline-fuchsia-900 | outline-color: var(--color-fuchsia-900); |
| outline-fuchsia-950 | outline-color: var(--color-fuchsia-950); |
| outline-pink-50 | outline-color: var(--color-pink-50); |
| outline-pink-100 | outline-color: var(--color-pink-100); |
| outline-pink-200 | outline-color: var(--color-pink-200); |
| outline-pink-300 | outline-color: var(--color-pink-300); |
| outline-pink-400 | outline-color: var(--color-pink-400); |
| outline-pink-500 | outline-color: var(--color-pink-500); |
| outline-pink-600 | outline-color: var(--color-pink-600); |
| outline-pink-700 | outline-color: var(--color-pink-700); |
| outline-pink-800 | outline-color: var(--color-pink-800); |
| outline-pink-900 | outline-color: var(--color-pink-900); |
| outline-pink-950 | outline-color: var(--color-pink-950); |
| outline-rose-50 | outline-color: var(--color-rose-50); |
| outline-rose-100 | outline-color: var(--color-rose-100); |
| outline-rose-200 | outline-color: var(--color-rose-200); |
| outline-rose-300 | outline-color: var(--color-rose-300); |
| outline-rose-400 | outline-color: var(--color-rose-400); |
| outline-rose-500 | outline-color: var(--color-rose-500); |
| outline-rose-600 | outline-color: var(--color-rose-600); |
| outline-rose-700 | outline-color: var(--color-rose-700); |
| outline-rose-800 | outline-color: var(--color-rose-800); |
| outline-rose-900 | outline-color: var(--color-rose-900); |
| outline-rose-950 | outline-color: var(--color-rose-950); |
| outline-slate-50 | outline-color: var(--color-slate-50); |
| outline-slate-100 | outline-color: var(--color-slate-100); |
| outline-slate-200 | outline-color: var(--color-slate-200); |
| outline-slate-300 | outline-color: var(--color-slate-300); |
| outline-slate-400 | outline-color: var(--color-slate-400); |
| outline-slate-500 | outline-color: var(--color-slate-500); |
| outline-slate-600 | outline-color: var(--color-slate-600); |
| outline-slate-700 | outline-color: var(--color-slate-700); |
| outline-slate-800 | outline-color: var(--color-slate-800); |
| outline-slate-900 | outline-color: var(--color-slate-900); |
| outline-slate-950 | outline-color: var(--color-slate-950); |
| outline-gray-50 | outline-color: var(--color-gray-50); |
| outline-gray-100 | outline-color: var(--color-gray-100); |
| outline-gray-200 | outline-color: var(--color-gray-200); |
| outline-gray-300 | outline-color: var(--color-gray-300); |
| outline-gray-400 | outline-color: var(--color-gray-400); |
| outline-gray-500 | outline-color: var(--color-gray-500); |
| outline-gray-600 | outline-color: var(--color-gray-600); |
| outline-gray-700 | outline-color: var(--color-gray-700); |
| outline-gray-800 | outline-color: var(--color-gray-800); |
| outline-gray-900 | outline-color: var(--color-gray-900); |
| outline-gray-950 | outline-color: var(--color-gray-950); |
| outline-zinc-50 | outline-color: var(--color-zinc-50); |
| outline-zinc-100 | outline-color: var(--color-zinc-100); |
| outline-zinc-200 | outline-color: var(--color-zinc-200); |
| outline-zinc-300 | outline-color: var(--color-zinc-300); |
| outline-zinc-400 | outline-color: var(--color-zinc-400); |
| outline-zinc-500 | outline-color: var(--color-zinc-500); |
| outline-zinc-600 | outline-color: var(--color-zinc-600); |
| outline-zinc-700 | outline-color: var(--color-zinc-700); |
| outline-zinc-800 | outline-color: var(--color-zinc-800); |
| outline-zinc-900 | outline-color: var(--color-zinc-900); |
| outline-zinc-950 | outline-color: var(--color-zinc-950); |
| outline-neutral-50 | outline-color: var(--color-neutral-50); |
| outline-neutral-100 | outline-color: var(--color-neutral-100); |
| outline-neutral-200 | outline-color: var(--color-neutral-200); |
| outline-neutral-300 | outline-color: var(--color-neutral-300); |
| outline-neutral-400 | outline-color: var(--color-neutral-400); |
| outline-neutral-500 | outline-color: var(--color-neutral-500); |
| outline-neutral-600 | outline-color: var(--color-neutral-600); |
| outline-neutral-700 | outline-color: var(--color-neutral-700); |
| outline-neutral-800 | outline-color: var(--color-neutral-800); |
| outline-neutral-900 | outline-color: var(--color-neutral-900); |
| outline-neutral-950 | outline-color: var(--color-neutral-950); |
| outline-stone-50 | outline-color: var(--color-stone-50); |
| outline-stone-100 | outline-color: var(--color-stone-100); |
| outline-stone-200 | outline-color: var(--color-stone-200); |
| outline-stone-300 | outline-color: var(--color-stone-300); |
| outline-stone-400 | outline-color: var(--color-stone-400); |
| outline-stone-500 | outline-color: var(--color-stone-500); |
| outline-stone-600 | outline-color: var(--color-stone-600); |
| outline-stone-700 | outline-color: var(--color-stone-700); |
| outline-stone-800 | outline-color: var(--color-stone-800); |
| outline-stone-900 | outline-color: var(--color-stone-900); |
| outline-stone-950 | outline-color: var(--color-stone-950); |
| outline-(<custom-property>) | outline-color: var(<custom-property>); |
| outline-[<value>] | outline-color: <value>; |

[Documentation](https://tailwindcss.com/docs/outline-color)

---

## outline-style

Utilities for controlling the style of an element's outline.

### Classes

| Class | Styles |
| --- | --- |
| outline-solid | outline-style: solid; |
| outline-dashed | outline-style: dashed; |
| outline-dotted | outline-style: dotted; |
| outline-double | outline-style: double; |
| outline-none | outline-style: none; |
| outline-hidden | outline: 2px solid transparent;<br>outline-offset: 2px; |

[Documentation](https://tailwindcss.com/docs/outline-style)

---

## outline-offset

Utilities for controlling the offset of an element's outline.

### Classes

| Class | Styles |
| --- | --- |
| outline-offset-<number> | outline-offset: <number>px; |
| -outline-offset-<number> | outline-offset: calc(<number>px * -1); |
| outline-offset-(<custom-property>) | outline-offset: var(<custom-property>); |
| outline-offset-[<value>] | outline-offset: <value>; |

[Documentation](https://tailwindcss.com/docs/outline-offset)

---

