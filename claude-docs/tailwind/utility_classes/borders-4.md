# Borders - Part 4

This document contains Tailwind CSS classes for Borders.

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

