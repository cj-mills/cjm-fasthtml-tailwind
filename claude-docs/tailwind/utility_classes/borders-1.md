# Borders - Part 1

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

| Class                               | Styles                                                       |
| ----------------------------------- | ------------------------------------------------------------ |
| border                              | border-width: 1px;                                           |
| border-<number>                     | border-width: <number>px;                                    |
| border-(length:<custom-property>)   | border-width: var(<custom-property>);                        |
| border-[<value>]                    | border-width: <value>;                                       |
| border-x                            | border-inline-width: 1px;                                    |
| border-x-<number>                   | border-inline-width: <number>px;                             |
| border-x-(length:<custom-property>) | border-inline-width: var(<custom-property>);                 |
| border-x-[<value>]                  | border-inline-width: <value>;                                |
| border-y                            | border-block-width: 1px;                                     |
| border-y-<number>                   | border-block-width: <number>px;                              |
| border-y-(length:<custom-property>) | border-block-width: var(<custom-property>);                  |
| border-y-[<value>]                  | border-block-width: <value>;                                 |
| border-s                            | border-inline-start-width: 1px;                              |
| border-s-<number>                   | border-inline-start-width: <number>px;                       |
| border-s-(length:<custom-property>) | border-inline-start-width: var(<custom-property>);           |
| border-s-[<value>]                  | border-inline-start-width: <value>;                          |
| border-e                            | border-inline-end-width: 1px;                                |
| border-e-<number>                   | border-inline-end-width: <number>px;                         |
| border-e-(length:<custom-property>) | border-inline-end-width: var(<custom-property>);             |
| border-e-[<value>]                  | border-inline-end-width: <value>;                            |
| border-t                            | border-top-width: 1px;                                       |
| border-t-<number>                   | border-top-width: <number>px;                                |
| border-t-(length:<custom-property>) | border-top-width: var(<custom-property>);                    |
| border-t-[<value>]                  | border-top-width: <value>;                                   |
| border-r                            | border-right-width: 1px;                                     |
| border-r-<number>                   | border-right-width: <number>px;                              |
| border-r-(length:<custom-property>) | border-right-width: var(<custom-property>);                  |
| border-r-[<value>]                  | border-right-width: <value>;                                 |
| border-b                            | border-bottom-width: 1px;                                    |
| border-b-<number>                   | border-bottom-width: <number>px;                             |
| border-b-(length:<custom-property>) | border-bottom-width: var(<custom-property>);                 |
| border-b-[<value>]                  | border-bottom-width: <value>;                                |
| border-l                            | border-left-width: 1px;                                      |
| border-l-<number>                   | border-left-width: <number>px;                               |
| border-l-(length:<custom-property>) | border-left-width: var(<custom-property>);                   |
| border-l-[<value>]                  | border-left-width: <value>;                                  |
| divide-x                            | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: 1px;<br>} |
| divide-x-<number>                   | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: <br><number><br>px;<br>} |
| divide-x-(length:<custom-property>) | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: var(<br><custom-property><br>);<br>} |
| divide-x-[<value>]                  | & > :not(:last-child) {<br>  border-inline-start-width: 0px;<br>  border-inline-end-width: <br><value><br>;<br>} |
| divide-y                            | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: 1px;<br>} |
| divide-y-<number>                   | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: <br><number><br>px;<br>} |
| divide-y-(length:<custom-property>) | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: var(<br><custom-property><br>);<br>} |
| divide-y-[<value>]                  | & > :not(:last-child) {<br>  border-top-width: 0px;<br>  border-bottom-width: <br><value><br>;<br>} |
| divide-x-reverse                    | --tw-divide-x-reverse: 1;                                    |
| divide-y-reverse                    | --tw-divide-y-reverse: 1;                                    |

[Documentation](https://tailwindcss.com/docs/border-width)

---

