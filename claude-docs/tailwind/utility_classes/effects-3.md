# Effects - Part 3

This document contains Tailwind CSS classes for Effects.

## text-shadow

Utilities for controlling the shadow of a text element.

### Classes

| Class | Styles |
| --- | --- |
| text-shadow-2xs | text-shadow: var(--text-shadow-2xs); /* 0px 1px 0px rgb(0 0 0 / 0.15) */ |
| text-shadow-xs | text-shadow: var(--text-shadow-xs); /* 0px 1px 1px rgb(0 0 0 / 0.2) */ |
| text-shadow-sm | text-shadow: var(--text-shadow-sm); /* 0px 1px 0px rgb(0 0 0 / 0.075), 0px 1px 1px rgb(0 0 0 / 0.075), 0px 2px 2px rgb(0 0 0 / 0.075) */ |
| text-shadow-md | text-shadow: var(--text-shadow-md); /* 0px 1px 1px rgb(0 0 0 / 0.1), 0px 1px 2px rgb(0 0 0 / 0.1), 0px 2px 4px rgb(0 0 0 / 0.1) */ |
| text-shadow-lg | text-shadow: var(--text-shadow-lg); /* 0px 1px 2px rgb(0 0 0 / 0.1), 0px 3px 2px rgb(0 0 0 / 0.1), 0px 4px 8px rgb(0 0 0 / 0.1) */ |
| text-shadow-none | text-shadow: none; |
| text-shadow-(<custom-property>) | --tw-inset-ring-color: var(--color-stone-950); text-shadow: var(<custom-property>); |
| text-shadow-(color:<custom-property>) | --tw-shadow-color var(<custom-property>); |
| text-shadow-[<value>] | text-shadow: <value>; |
| text-shadow-inherit | --tw-shadow-color inherit; |
| text-shadow-current | --tw-shadow-color currentColor; |
| text-shadow-transparent | --tw-shadow-color transparent; |
| text-shadow-black | --tw-text-shadow-color var(--color-black); /* #000 */ |
| text-shadow-white | --tw-text-shadow-color var(--color-white); /* #fff */ |
| text-shadow-red-50 | --tw-text-shadow-color var(--color-red-50); |
| text-shadow-red-100 | --tw-text-shadow-color var(--color-red-100); |
| text-shadow-red-200 | --tw-text-shadow-color var(--color-red-200); |
| text-shadow-red-300 | --tw-text-shadow-color var(--color-red-300); |
| text-shadow-red-400 | --tw-text-shadow-color var(--color-red-400); |
| text-shadow-red-500 | --tw-text-shadow-color var(--color-red-500); |
| text-shadow-red-600 | --tw-text-shadow-color var(--color-red-600); |
| text-shadow-red-700 | --tw-text-shadow-color var(--color-red-700); |
| text-shadow-red-800 | --tw-text-shadow-color var(--color-red-800); |
| text-shadow-red-900 | --tw-text-shadow-color var(--color-red-900); |
| text-shadow-red-950 | --tw-text-shadow-color var(--color-red-950); |
| text-shadow-orange-50 | --tw-text-shadow-color var(--color-orange-50); |
| text-shadow-orange-100 | --tw-text-shadow-color var(--color-orange-100); |
| text-shadow-orange-200 | --tw-text-shadow-color var(--color-orange-200); |
| text-shadow-orange-300 | --tw-text-shadow-color var(--color-orange-300); |
| text-shadow-orange-400 | --tw-text-shadow-color var(--color-orange-400); |
| text-shadow-orange-500 | --tw-text-shadow-color var(--color-orange-500); |
| text-shadow-orange-600 | --tw-text-shadow-color var(--color-orange-600); |
| text-shadow-orange-700 | --tw-text-shadow-color var(--color-orange-700); |
| text-shadow-orange-800 | --tw-text-shadow-color var(--color-orange-800); |
| text-shadow-orange-900 | --tw-text-shadow-color var(--color-orange-900); |
| text-shadow-orange-950 | --tw-text-shadow-color var(--color-orange-950); |
| text-shadow-amber-50 | --tw-text-shadow-color var(--color-amber-50); |
| text-shadow-amber-100 | --tw-text-shadow-color var(--color-amber-100); |
| text-shadow-amber-200 | --tw-text-shadow-color var(--color-amber-200); |
| text-shadow-amber-300 | --tw-text-shadow-color var(--color-amber-300); |
| text-shadow-amber-400 | --tw-text-shadow-color var(--color-amber-400); |
| text-shadow-amber-500 | --tw-text-shadow-color var(--color-amber-500); |
| text-shadow-amber-600 | --tw-text-shadow-color var(--color-amber-600); |
| text-shadow-amber-700 | --tw-text-shadow-color var(--color-amber-700); |
| text-shadow-amber-800 | --tw-text-shadow-color var(--color-amber-800); |
| text-shadow-amber-900 | --tw-text-shadow-color var(--color-amber-900); |
| text-shadow-amber-950 | --tw-text-shadow-color var(--color-amber-950); |
| text-shadow-yellow-50 | --tw-text-shadow-color var(--color-yellow-50); |
| text-shadow-yellow-100 | --tw-text-shadow-color var(--color-yellow-100); |
| text-shadow-yellow-200 | --tw-text-shadow-color var(--color-yellow-200); |
| text-shadow-yellow-300 | --tw-text-shadow-color var(--color-yellow-300); |
| text-shadow-yellow-400 | --tw-text-shadow-color var(--color-yellow-400); |
| text-shadow-yellow-500 | --tw-text-shadow-color var(--color-yellow-500); |
| text-shadow-yellow-600 | --tw-text-shadow-color var(--color-yellow-600); |
| text-shadow-yellow-700 | --tw-text-shadow-color var(--color-yellow-700); |
| text-shadow-yellow-800 | --tw-text-shadow-color var(--color-yellow-800); |
| text-shadow-yellow-900 | --tw-text-shadow-color var(--color-yellow-900); |
| text-shadow-yellow-950 | --tw-text-shadow-color var(--color-yellow-950); |
| text-shadow-lime-50 | --tw-text-shadow-color var(--color-lime-50); |
| text-shadow-lime-100 | --tw-text-shadow-color var(--color-lime-100); |
| text-shadow-lime-200 | --tw-text-shadow-color var(--color-lime-200); |
| text-shadow-lime-300 | --tw-text-shadow-color var(--color-lime-300); |
| text-shadow-lime-400 | --tw-text-shadow-color var(--color-lime-400); |
| text-shadow-lime-500 | --tw-text-shadow-color var(--color-lime-500); |
| text-shadow-lime-600 | --tw-text-shadow-color var(--color-lime-600); |
| text-shadow-lime-700 | --tw-text-shadow-color var(--color-lime-700); |
| text-shadow-lime-800 | --tw-text-shadow-color var(--color-lime-800); |
| text-shadow-lime-900 | --tw-text-shadow-color var(--color-lime-900); |
| text-shadow-lime-950 | --tw-text-shadow-color var(--color-lime-950); |
| text-shadow-green-50 | --tw-text-shadow-color var(--color-green-50); |
| text-shadow-green-100 | --tw-text-shadow-color var(--color-green-100); |
| text-shadow-green-200 | --tw-text-shadow-color var(--color-green-200); |
| text-shadow-green-300 | --tw-text-shadow-color var(--color-green-300); |
| text-shadow-green-400 | --tw-text-shadow-color var(--color-green-400); |
| text-shadow-green-500 | --tw-text-shadow-color var(--color-green-500); |
| text-shadow-green-600 | --tw-text-shadow-color var(--color-green-600); |
| text-shadow-green-700 | --tw-text-shadow-color var(--color-green-700); |
| text-shadow-green-800 | --tw-text-shadow-color var(--color-green-800); |
| text-shadow-green-900 | --tw-text-shadow-color var(--color-green-900); |
| text-shadow-green-950 | --tw-text-shadow-color var(--color-green-950); |
| text-shadow-emerald-50 | --tw-text-shadow-color var(--color-emerald-50); |
| text-shadow-emerald-100 | --tw-text-shadow-color var(--color-emerald-100); |
| text-shadow-emerald-200 | --tw-text-shadow-color var(--color-emerald-200); |
| text-shadow-emerald-300 | --tw-text-shadow-color var(--color-emerald-300); |
| text-shadow-emerald-400 | --tw-text-shadow-color var(--color-emerald-400); |
| text-shadow-emerald-500 | --tw-text-shadow-color var(--color-emerald-500); |
| text-shadow-emerald-600 | --tw-text-shadow-color var(--color-emerald-600); |
| text-shadow-emerald-700 | --tw-text-shadow-color var(--color-emerald-700); |
| text-shadow-emerald-800 | --tw-text-shadow-color var(--color-emerald-800); |
| text-shadow-emerald-900 | --tw-text-shadow-color var(--color-emerald-900); |
| text-shadow-emerald-950 | --tw-text-shadow-color var(--color-emerald-950); |
| text-shadow-teal-50 | --tw-text-shadow-color var(--color-teal-50); |
| text-shadow-teal-100 | --tw-text-shadow-color var(--color-teal-100); |
| text-shadow-teal-200 | --tw-text-shadow-color var(--color-teal-200); |
| text-shadow-teal-300 | --tw-text-shadow-color var(--color-teal-300); |
| text-shadow-teal-400 | --tw-text-shadow-color var(--color-teal-400); |
| text-shadow-teal-500 | --tw-text-shadow-color var(--color-teal-500); |
| text-shadow-teal-600 | --tw-text-shadow-color var(--color-teal-600); |
| text-shadow-teal-700 | --tw-text-shadow-color var(--color-teal-700); |
| text-shadow-teal-800 | --tw-text-shadow-color var(--color-teal-800); |
| text-shadow-teal-900 | --tw-text-shadow-color var(--color-teal-900); |
| text-shadow-teal-950 | --tw-text-shadow-color var(--color-teal-950); |
| text-shadow-cyan-50 | --tw-text-shadow-color var(--color-cyan-50); |
| text-shadow-cyan-100 | --tw-text-shadow-color var(--color-cyan-100); |
| text-shadow-cyan-200 | --tw-text-shadow-color var(--color-cyan-200); |
| text-shadow-cyan-300 | --tw-text-shadow-color var(--color-cyan-300); |
| text-shadow-cyan-400 | --tw-text-shadow-color var(--color-cyan-400); |
| text-shadow-cyan-500 | --tw-text-shadow-color var(--color-cyan-500); |
| text-shadow-cyan-600 | --tw-text-shadow-color var(--color-cyan-600); |
| text-shadow-cyan-700 | --tw-text-shadow-color var(--color-cyan-700); |
| text-shadow-cyan-800 | --tw-text-shadow-color var(--color-cyan-800); |
| text-shadow-cyan-900 | --tw-text-shadow-color var(--color-cyan-900); |
| text-shadow-cyan-950 | --tw-text-shadow-color var(--color-cyan-950); |
| text-shadow-sky-50 | --tw-text-shadow-color var(--color-sky-50); |
| text-shadow-sky-100 | --tw-text-shadow-color var(--color-sky-100); |
| text-shadow-sky-200 | --tw-text-shadow-color var(--color-sky-200); |
| text-shadow-sky-300 | --tw-text-shadow-color var(--color-sky-300); |
| text-shadow-sky-400 | --tw-text-shadow-color var(--color-sky-400); |
| text-shadow-sky-500 | --tw-text-shadow-color var(--color-sky-500); |
| text-shadow-sky-600 | --tw-text-shadow-color var(--color-sky-600); |
| text-shadow-sky-700 | --tw-text-shadow-color var(--color-sky-700); |
| text-shadow-sky-800 | --tw-text-shadow-color var(--color-sky-800); |
| text-shadow-sky-900 | --tw-text-shadow-color var(--color-sky-900); |
| text-shadow-sky-950 | --tw-text-shadow-color var(--color-sky-950); |
| text-shadow-blue-50 | --tw-text-shadow-color var(--color-blue-50); |
| text-shadow-blue-100 | --tw-text-shadow-color var(--color-blue-100); |
| text-shadow-blue-200 | --tw-text-shadow-color var(--color-blue-200); |
| text-shadow-blue-300 | --tw-text-shadow-color var(--color-blue-300); |
| text-shadow-blue-400 | --tw-text-shadow-color var(--color-blue-400); |
| text-shadow-blue-500 | --tw-text-shadow-color var(--color-blue-500); |
| text-shadow-blue-600 | --tw-text-shadow-color var(--color-blue-600); |
| text-shadow-blue-700 | --tw-text-shadow-color var(--color-blue-700); |
| text-shadow-blue-800 | --tw-text-shadow-color var(--color-blue-800); |
| text-shadow-blue-900 | --tw-text-shadow-color var(--color-blue-900); |
| text-shadow-blue-950 | --tw-text-shadow-color var(--color-blue-950); |
| text-shadow-indigo-50 | --tw-text-shadow-color var(--color-indigo-50); |
| text-shadow-indigo-100 | --tw-text-shadow-color var(--color-indigo-100); |
| text-shadow-indigo-200 | --tw-text-shadow-color var(--color-indigo-200); |
| text-shadow-indigo-300 | --tw-text-shadow-color var(--color-indigo-300); |
| text-shadow-indigo-400 | --tw-text-shadow-color var(--color-indigo-400); |
| text-shadow-indigo-500 | --tw-text-shadow-color var(--color-indigo-500); |
| text-shadow-indigo-600 | --tw-text-shadow-color var(--color-indigo-600); |
| text-shadow-indigo-700 | --tw-text-shadow-color var(--color-indigo-700); |
| text-shadow-indigo-800 | --tw-text-shadow-color var(--color-indigo-800); |
| text-shadow-indigo-900 | --tw-text-shadow-color var(--color-indigo-900); |
| text-shadow-indigo-950 | --tw-text-shadow-color var(--color-indigo-950); |
| text-shadow-violet-50 | --tw-text-shadow-color var(--color-violet-50); |
| text-shadow-violet-100 | --tw-text-shadow-color var(--color-violet-100); |
| text-shadow-violet-200 | --tw-text-shadow-color var(--color-violet-200); |
| text-shadow-violet-300 | --tw-text-shadow-color var(--color-violet-300); |
| text-shadow-violet-400 | --tw-text-shadow-color var(--color-violet-400); |
| text-shadow-violet-500 | --tw-text-shadow-color var(--color-violet-500); |
| text-shadow-violet-600 | --tw-text-shadow-color var(--color-violet-600); |
| text-shadow-violet-700 | --tw-text-shadow-color var(--color-violet-700); |
| text-shadow-violet-800 | --tw-text-shadow-color var(--color-violet-800); |
| text-shadow-violet-900 | --tw-text-shadow-color var(--color-violet-900); |
| text-shadow-violet-950 | --tw-text-shadow-color var(--color-violet-950); |
| text-shadow-purple-50 | --tw-text-shadow-color var(--color-purple-50); |
| text-shadow-purple-100 | --tw-text-shadow-color var(--color-purple-100); |
| text-shadow-purple-200 | --tw-text-shadow-color var(--color-purple-200); |
| text-shadow-purple-300 | --tw-text-shadow-color var(--color-purple-300); |
| text-shadow-purple-400 | --tw-text-shadow-color var(--color-purple-400); |
| text-shadow-purple-500 | --tw-text-shadow-color var(--color-purple-500); |
| text-shadow-purple-600 | --tw-text-shadow-color var(--color-purple-600); |
| text-shadow-purple-700 | --tw-text-shadow-color var(--color-purple-700); |
| text-shadow-purple-800 | --tw-text-shadow-color var(--color-purple-800); |
| text-shadow-purple-900 | --tw-text-shadow-color var(--color-purple-900); |
| text-shadow-purple-950 | --tw-text-shadow-color var(--color-purple-950); |
| text-shadow-fuchsia-50 | --tw-text-shadow-color var(--color-fuchsia-50); |
| text-shadow-fuchsia-100 | --tw-text-shadow-color var(--color-fuchsia-100); |
| text-shadow-fuchsia-200 | --tw-text-shadow-color var(--color-fuchsia-200); |
| text-shadow-fuchsia-300 | --tw-text-shadow-color var(--color-fuchsia-300); |
| text-shadow-fuchsia-400 | --tw-text-shadow-color var(--color-fuchsia-400); |
| text-shadow-fuchsia-500 | --tw-text-shadow-color var(--color-fuchsia-500); |
| text-shadow-fuchsia-600 | --tw-text-shadow-color var(--color-fuchsia-600); |
| text-shadow-fuchsia-700 | --tw-text-shadow-color var(--color-fuchsia-700); |
| text-shadow-fuchsia-800 | --tw-text-shadow-color var(--color-fuchsia-800); |
| text-shadow-fuchsia-900 | --tw-text-shadow-color var(--color-fuchsia-900); |
| text-shadow-fuchsia-950 | --tw-text-shadow-color var(--color-fuchsia-950); |
| text-shadow-pink-50 | --tw-text-shadow-color var(--color-pink-50); |
| text-shadow-pink-100 | --tw-text-shadow-color var(--color-pink-100); |
| text-shadow-pink-200 | --tw-text-shadow-color var(--color-pink-200); |
| text-shadow-pink-300 | --tw-text-shadow-color var(--color-pink-300); |
| text-shadow-pink-400 | --tw-text-shadow-color var(--color-pink-400); |
| text-shadow-pink-500 | --tw-text-shadow-color var(--color-pink-500); |
| text-shadow-pink-600 | --tw-text-shadow-color var(--color-pink-600); |
| text-shadow-pink-700 | --tw-text-shadow-color var(--color-pink-700); |
| text-shadow-pink-800 | --tw-text-shadow-color var(--color-pink-800); |
| text-shadow-pink-900 | --tw-text-shadow-color var(--color-pink-900); |
| text-shadow-pink-950 | --tw-text-shadow-color var(--color-pink-950); |
| text-shadow-rose-50 | --tw-text-shadow-color var(--color-rose-50); |
| text-shadow-rose-100 | --tw-text-shadow-color var(--color-rose-100); |
| text-shadow-rose-200 | --tw-text-shadow-color var(--color-rose-200); |
| text-shadow-rose-300 | --tw-text-shadow-color var(--color-rose-300); |
| text-shadow-rose-400 | --tw-text-shadow-color var(--color-rose-400); |
| text-shadow-rose-500 | --tw-text-shadow-color var(--color-rose-500); |
| text-shadow-rose-600 | --tw-text-shadow-color var(--color-rose-600); |
| text-shadow-rose-700 | --tw-text-shadow-color var(--color-rose-700); |
| text-shadow-rose-800 | --tw-text-shadow-color var(--color-rose-800); |
| text-shadow-rose-900 | --tw-text-shadow-color var(--color-rose-900); |
| text-shadow-rose-950 | --tw-text-shadow-color var(--color-rose-950); |
| text-shadow-slate-50 | --tw-text-shadow-color var(--color-slate-50); |
| text-shadow-slate-100 | --tw-text-shadow-color var(--color-slate-100); |
| text-shadow-slate-200 | --tw-text-shadow-color var(--color-slate-200); |
| text-shadow-slate-300 | --tw-text-shadow-color var(--color-slate-300); |
| text-shadow-slate-400 | --tw-text-shadow-color var(--color-slate-400); |
| text-shadow-slate-500 | --tw-text-shadow-color var(--color-slate-500); |
| text-shadow-slate-600 | --tw-text-shadow-color var(--color-slate-600); |
| text-shadow-slate-700 | --tw-text-shadow-color var(--color-slate-700); |
| text-shadow-slate-800 | --tw-text-shadow-color var(--color-slate-800); |
| text-shadow-slate-900 | --tw-text-shadow-color var(--color-slate-900); |
| text-shadow-slate-950 | --tw-text-shadow-color var(--color-slate-950); |
| text-shadow-gray-50 | --tw-text-shadow-color var(--color-gray-50); |
| text-shadow-gray-100 | --tw-text-shadow-color var(--color-gray-100); |
| text-shadow-gray-200 | --tw-text-shadow-color var(--color-gray-200); |
| text-shadow-gray-300 | --tw-text-shadow-color var(--color-gray-300); |
| text-shadow-gray-400 | --tw-text-shadow-color var(--color-gray-400); |
| text-shadow-gray-500 | --tw-text-shadow-color var(--color-gray-500); |
| text-shadow-gray-600 | --tw-text-shadow-color var(--color-gray-600); |
| text-shadow-gray-700 | --tw-text-shadow-color var(--color-gray-700); |
| text-shadow-gray-800 | --tw-text-shadow-color var(--color-gray-800); |
| text-shadow-gray-900 | --tw-text-shadow-color var(--color-gray-900); |
| text-shadow-gray-950 | --tw-text-shadow-color var(--color-gray-950); |
| text-shadow-zinc-50 | --tw-text-shadow-color var(--color-zinc-50); |
| text-shadow-zinc-100 | --tw-text-shadow-color var(--color-zinc-100); |
| text-shadow-zinc-200 | --tw-text-shadow-color var(--color-zinc-200); |
| text-shadow-zinc-300 | --tw-text-shadow-color var(--color-zinc-300); |
| text-shadow-zinc-400 | --tw-text-shadow-color var(--color-zinc-400); |
| text-shadow-zinc-500 | --tw-text-shadow-color var(--color-zinc-500); |
| text-shadow-zinc-600 | --tw-text-shadow-color var(--color-zinc-600); |
| text-shadow-zinc-700 | --tw-text-shadow-color var(--color-zinc-700); |
| text-shadow-zinc-800 | --tw-text-shadow-color var(--color-zinc-800); |
| text-shadow-zinc-900 | --tw-text-shadow-color var(--color-zinc-900); |
| text-shadow-zinc-950 | --tw-text-shadow-color var(--color-zinc-950); |
| text-shadow-neutral-50 | --tw-text-shadow-color var(--color-neutral-50); |
| text-shadow-neutral-100 | --tw-text-shadow-color var(--color-neutral-100); |
| text-shadow-neutral-200 | --tw-text-shadow-color var(--color-neutral-200); |
| text-shadow-neutral-300 | --tw-text-shadow-color var(--color-neutral-300); |
| text-shadow-neutral-400 | --tw-text-shadow-color var(--color-neutral-400); |
| text-shadow-neutral-500 | --tw-text-shadow-color var(--color-neutral-500); |
| text-shadow-neutral-600 | --tw-text-shadow-color var(--color-neutral-600); |
| text-shadow-neutral-700 | --tw-text-shadow-color var(--color-neutral-700); |
| text-shadow-neutral-800 | --tw-text-shadow-color var(--color-neutral-800); |
| text-shadow-neutral-900 | --tw-text-shadow-color var(--color-neutral-900); |
| text-shadow-neutral-950 | --tw-text-shadow-color var(--color-neutral-950); |
| text-shadow-stone-50 | --tw-text-shadow-color var(--color-stone-50); |
| text-shadow-stone-100 | --tw-text-shadow-color var(--color-stone-100); |
| text-shadow-stone-200 | --tw-text-shadow-color var(--color-stone-200); |
| text-shadow-stone-300 | --tw-text-shadow-color var(--color-stone-300); |
| text-shadow-stone-400 | --tw-text-shadow-color var(--color-stone-400); |
| text-shadow-stone-500 | --tw-text-shadow-color var(--color-stone-500); |
| text-shadow-stone-600 | --tw-text-shadow-color var(--color-stone-600); |
| text-shadow-stone-700 | --tw-text-shadow-color var(--color-stone-700); |
| text-shadow-stone-800 | --tw-text-shadow-color var(--color-stone-800); |
| text-shadow-stone-900 | --tw-text-shadow-color var(--color-stone-900); |
| text-shadow-stone-950 | --tw-text-shadow-color var(--color-stone-950); |

[Documentation](https://tailwindcss.com/docs/text-shadow)

---

## opacity

Utilities for controlling the opacity of an element.

### Classes

| Class | Styles |
| --- | --- |
| opacity-<number> | opacity: <number>%; |
| opacity-(<custom-property>) | opacity: var(<custom-property>); |
| opacity-[<value>] | opacity: <value>; |

[Documentation](https://tailwindcss.com/docs/opacity)

---

## mix-blend-mode

Utilities for controlling how an element should blend with the background.

### Classes

| Class | Styles |
| --- | --- |
| mix-blend-normal | mix-blend-mode: normal; |
| mix-blend-multiply | mix-blend-mode: multiply; |
| mix-blend-screen | mix-blend-mode: screen; |
| mix-blend-overlay | mix-blend-mode: overlay; |
| mix-blend-darken | mix-blend-mode: darken; |
| mix-blend-lighten | mix-blend-mode: lighten; |
| mix-blend-color-dodge | mix-blend-mode: color-dodge; |
| mix-blend-color-burn | mix-blend-mode: color-burn; |
| mix-blend-hard-light | mix-blend-mode: hard-light; |
| mix-blend-soft-light | mix-blend-mode: soft-light; |
| mix-blend-difference | mix-blend-mode: difference; |
| mix-blend-exclusion | mix-blend-mode: exclusion; |
| mix-blend-hue | mix-blend-mode: hue; |
| mix-blend-saturation | mix-blend-mode: saturation; |
| mix-blend-color | mix-blend-mode: color; |
| mix-blend-luminosity | mix-blend-mode: luminosity; |
| mix-blend-plus-darker | mix-blend-mode: plus-darker; |
| mix-blend-plus-lighter | mix-blend-mode: plus-lighter; |

[Documentation](https://tailwindcss.com/docs/mix-blend-mode)

---

## background-blend-mode

Utilities for controlling how an element's background image should blend with its background color.

### Classes

| Class | Styles |
| --- | --- |
| bg-blend-normal | background-blend-mode: normal; |
| bg-blend-multiply | background-blend-mode: multiply; |
| bg-blend-screen | background-blend-mode: screen; |
| bg-blend-overlay | background-blend-mode: overlay; |
| bg-blend-darken | background-blend-mode: darken; |
| bg-blend-lighten | background-blend-mode: lighten; |
| bg-blend-color-dodge | background-blend-mode: color-dodge; |
| bg-blend-color-burn | background-blend-mode: color-burn; |
| bg-blend-hard-light | background-blend-mode: hard-light; |
| bg-blend-soft-light | background-blend-mode: soft-light; |
| bg-blend-difference | background-blend-mode: difference; |
| bg-blend-exclusion | background-blend-mode: exclusion; |
| bg-blend-hue | background-blend-mode: hue; |
| bg-blend-saturation | background-blend-mode: saturation; |
| bg-blend-color | background-blend-mode: color; |
| bg-blend-luminosity | background-blend-mode: luminosity; |

[Documentation](https://tailwindcss.com/docs/background-blend-mode)

---

## mask-clip

Utilities for controlling the bounding box of an element's mask.

### Classes

| Class | Styles |
| --- | --- |
| mask-clip-border | mask-clip: border-box; |
| mask-clip-padding | mask-clip: padding-box; |
| mask-clip-content | mask-clip: content-box; |
| mask-clip-fill | mask-clip: fill-box; |
| mask-clip-stroke | mask-clip: stroke-box; |
| mask-clip-view | mask-clip: view-box; |
| mask-no-clip | mask-clip: no-clip; |

[Documentation](https://tailwindcss.com/docs/mask-clip)

---

## mask-composite

Utilities for controlling how multiple masks are combined together.

### Classes

| Class | Styles |
| --- | --- |
| mask-add | mask-composite: add; |
| mask-subtract | mask-composite: subtract; |
| mask-intersect | mask-composite: intersect; |
| mask-exclude | mask-composite: exclude; |

[Documentation](https://tailwindcss.com/docs/mask-composite)

---

## mask-image

Utilities for controlling an element's mask image.

### Classes

| Class | Styles |
| --- | --- |
| mask-[<value>] | mask-image: <value>; |
| mask-(<custom-property>) | mask-image: var(<custom-property>); |
| mask-none | mask-image: none; |
| mask-linear-<number> | mask-image: linear-gradient(<number>deg, black var(--tw-mask-linear-from)), transparent var(--tw-mask-linear-to)); |
| -mask-linear-<number> | mask-image: linear-gradient(calc(<number>deg * -1), black var(--tw-mask-linear-from)), transparent var(--tw-mask-linear-to)); |
| mask-linear-from-<number> | mask-image: linear-gradient(var(--tw-mask-linear-position), black calc(var(--spacing * <number>)), transparent var(--tw-mask-linear-to)); |
| mask-linear-from-<percentage> | mask-image: linear-gradient(var(--tw-mask-linear-position), black <percentage>, transparent var(--tw-mask-linear-to)); |
| mask-linear-from-<color> | mask-image: linear-gradient(var(--tw-mask-linear-position), <color> var(--tw-mask-linear-from), transparent var(--tw-mask-linear-to)); |
| mask-linear-from-(<custom-property>) | mask-image: linear-gradient(var(--tw-mask-linear-position), black <custom-property>, transparent var(--tw-mask-linear-to)); |
| mask-linear-from-[<value>] | mask-image: linear-gradient(var(--tw-mask-linear-position), black <value>, transparent var(--tw-mask-linear-to)); |
| mask-linear-to-<number> | mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent calc(var(--spacing * <number>))); |
| mask-linear-to-<percentage> | mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent <percentage>); |
| mask-linear-to-<color> | mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), <color> var(--tw-mask-linear-to)); |
| mask-linear-to-(<custom-property>) | mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent var(<custom-property>)); |
| mask-linear-to-[<value>] | mask-image: linear-gradient(var(--tw-mask-linear-position), black var(--tw-mask-linear-from), transparent <value>); |
| mask-t-from-<number> | mask-image: linear-gradient(to top, black calc(var(--spacing * <number>)), transparent var(--tw-mask-top-to)); |
| mask-t-from-<percentage> | mask-image: linear-gradient(to top, black <percentage>, transparent var(--tw-mask-top-to)); |
| mask-t-from-<color> | mask-image: linear-gradient(to top, <color> var(--tw-mask-top-from), transparent var(--tw-mask-top-to)); |
| mask-t-from-(<custom-property>) | mask-image: linear-gradient(to top, black var(<custom-property>), transparent var(--tw-mask-top-to)); |
| mask-t-from-[<value>] | mask-image: linear-gradient(to top, black <value>, transparent var(--tw-mask-top-to)); |
| mask-t-to-<number> | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent calc(var(--spacing * <number>)); |
| mask-t-to-<percentage> | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <percentage>); |
| mask-t-to-<color> | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), <color> var(--tw-mask-top-to)); |
| mask-t-to-(<custom-property>) | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent var(<custom-property>)); |
| mask-t-to-[<value>] | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <value>); |
| mask-r-from-<number> | mask-image: linear-gradient(to right, black calc(var(--spacing * <number>)), transparent var(--tw-mask-right-to)); |
| mask-r-from-<percentage> | mask-image: linear-gradient(to right, black <percentage>, transparent var(--tw-mask-right-to)); |
| mask-r-from-<color> | mask-image: linear-gradient(to right, <color> var(--tw-mask-right-from), transparent var(--tw-mask-right-to)); |
| mask-r-from-(<custom-property>) | mask-image: linear-gradient(to right, black var(<custom-property>), transparent var(--tw-mask-right-to)); |
| mask-r-from-[<value>] | mask-image: linear-gradient(to right, black <value>, transparent var(--tw-mask-right-to)); |
| mask-r-to-<number> | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent calc(var(--spacing * <number>)); |
| mask-r-to-<percentage> | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <percentage>); |
| mask-r-to-<color> | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), <color> var(--tw-mask-right-to)); |
| mask-r-to-(<custom-property>) | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent var(<custom-property>)); |
| mask-r-to-[<value>] | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <value>); |
| mask-b-from-<number> | mask-image: linear-gradient(to bottom, black calc(var(--spacing * <number>)), transparent var(--tw-mask-bottom-to)); |
| mask-b-from-<percentage> | mask-image: linear-gradient(to bottom, black <percentage>, transparent var(--tw-mask-bottom-to)); |
| mask-b-from-<color> | mask-image: linear-gradient(to bottom, <color> var(--tw-mask-bottom-from), transparent var(--tw-mask-bottom-to)); |
| mask-b-from-(<custom-property>) | mask-image: linear-gradient(to bottom, black var(<custom-property>), transparent var(--tw-mask-bottom-to)); |
| mask-b-from-[<value>] | mask-image: linear-gradient(to bottom, black <value>, transparent var(--tw-mask-bottom-to)); |
| mask-b-to-<number> | mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent calc(var(--spacing * <number>)); |
| mask-b-to-<percentage> | mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <percentage>); |
| mask-b-to-<color> | mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), <color> var(--tw-mask-bottom-to)); |
| mask-b-to-(<custom-property>) | mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent var(<custom-property>)); |
| mask-b-to-[<value>] | mask-image: linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <value>); |
| mask-l-from-<number> | mask-image: linear-gradient(to left, black calc(var(--spacing * <number>)), transparent var(--tw-mask-left-to)); |
| mask-l-from-<percentage> | mask-image: linear-gradient(to left, black <percentage>, transparent var(--tw-mask-left-to)); |
| mask-l-from-<color> | mask-image: linear-gradient(to left, <color> var(--tw-mask-left-from), transparent var(--tw-mask-left-to)); |
| mask-l-from-(<custom-property>) | mask-image: linear-gradient(to left, black var(<custom-property>), transparent var(--tw-mask-left-to)); |
| mask-l-from-[<value>] | mask-image: linear-gradient(to left, black <value>, transparent var(--tw-mask-left-to)); |
| mask-l-to-<number> | mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent calc(var(--spacing * <number>)); |
| mask-l-to-<percentage> | mask-image: linear-gradient(to bottom, black var(--tw-mask-left-from), transparent <percentage>); |
| mask-l-to-<color> | mask-image: linear-gradient(to bottom, black var(--tw-mask-left-from), <color> var(--tw-mask-left-to)); |
| mask-l-to-(<custom-property>) | mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent var(<custom-property>)); |
| mask-l-to-[<value>] | mask-image: linear-gradient(to left, black var(--tw-mask-left-from), transparent <value>); |
| mask-y-from-<number> | mask-image: linear-gradient(to top, black calc(var(--spacing * <br><number><br>)), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black calc(var(--spacing * <br><number><br>)), transparent var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-from-<percentage> | mask-image: linear-gradient(to top, black <br><percentage><br>, transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black <br><percentage><br>, transparent var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-from-<color> | mask-image: linear-gradient(to top, <br><color><br> var(--tw-mask-top-from), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, <br><color><br> var(--tw-mask-bottom-from), transparent var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-from-(<custom-property>) | mask-image: linear-gradient(to top, black var(<br><custom-property><br>), transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black var(<br><custom-property><br>), transparent var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-from-[<value>] | mask-image: linear-gradient(to top, black <br><value><br>, transparent var(--tw-mask-top-to)), linear-gradient(to bottom, black <br><value><br>, transparent var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-to-<number> | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent calc(var(--spacing * <br><number><br>)), linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent calc(var(--spacing * <br><number><br>));<br>mask-composite: intersect; |
| mask-y-to-<percentage> | mask-image: linear-gradient(to bottom, black var(--tw-mask-top-from), transparent <br><percentage><br>), linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <br><percentage><br>);<br>mask-composite: intersect; |
| mask-y-to-<color> | mask-image: linear-gradient(to bottom, black var(--tw-mask-top-from), <br><color><br> var(--tw-mask-top-to)), linear-gradient(to bottom, black var(--tw-mask-bottom-from), <br><color><br> var(--tw-mask-bottom-to));<br>mask-composite: intersect; |
| mask-y-to-(<custom-property>) | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent var(<br><custom-property><br>)),linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent var(<br><custom-property><br>));<br>mask-composite: intersect; |
| mask-y-to-[<value>] | mask-image: linear-gradient(to top, black var(--tw-mask-top-from), transparent <br><value><br>),linear-gradient(to bottom, black var(--tw-mask-bottom-from), transparent <br><value><br>);<br>mask-composite: intersect; |
| mask-x-from-<number> | mask-image: linear-gradient(to right, black calc(var(--spacing * <br><number><br>)), transparent var(--tw-mask-right-to)), linear-gradient(to left, black calc(var(--spacing * <br><number><br>)), transparent var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-from-<percentage> | mask-image: linear-gradient(to right, black <br><percentage><br>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <br><percentage><br>, transparent var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-from-<color> | mask-image: linear-gradient(to right, <br><color><br> var(--tw-mask-right-from), transparent var(--tw-mask-right-to)), linear-gradient(to left, <br><color><br>  var(--tw-mask-left-from), transparent var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-from-(<custom-property>) | mask-image: linear-gradient(to right, black var(<br><custom-property><br>), transparent var(--tw-mask-right-to)), linear-gradient(to left, black var(<br><custom-property><br>), transparent var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-from-[<value>] | mask-image: linear-gradient(to right, black <br><value><br>, transparent var(--tw-mask-right-to)), linear-gradient(to left, black <br><value><br>, transparent var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-to-<number> | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent calc(var(--spacing * <br><number><br>)), linear-gradient(to left, black var(--tw-mask-left-from), transparent calc(var(--spacing * <br><number><br>));<br>mask-composite: intersect; |
| mask-x-to-<percentage> | mask-image: linear-gradient(to left, black var(--tw-mask-right-from), transparent <br><percentage><br>), linear-gradient(to left, black var(--tw-mask-left-from), transparent <br><percentage><br>);<br>mask-composite: intersect; |
| mask-x-to-<color> | mask-image: linear-gradient(to left, black var(--tw-mask-right-from), <br><color><br> var(--tw-mask-right-to)), linear-gradient(to left, black var(--tw-mask-left-from), <br><color><br> var(--tw-mask-left-to));<br>mask-composite: intersect; |
| mask-x-to-(<custom-property>) | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent var(<br><custom-property><br>)),linear-gradient(to left, black var(--tw-mask-left-from), transparent var(<br><custom-property><br>));<br>mask-composite: intersect; |
| mask-x-to-[<value>] | mask-image: linear-gradient(to right, black var(--tw-mask-right-from), transparent <br><value><br>),linear-gradient(to left, black var(--tw-mask-left-from), transparent <br><value><br>);<br>mask-composite: intersect; |
| mask-radial-[<value>] | mask-image: radial-gradient(<value>); |
| mask-radial-[<size>] | --tw-mask-radial-size: <size>; |
| mask-radial-[<size>_<size>] | --tw-mask-radial-size: <size> <size>; |
| mask-radial-from-<number> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black calc(var(--spacing * <number>)), transparent var(--tw-mask-radial-to)); |
| mask-radial-from-<percentage> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <percentage>, transparent var(--tw-mask-radial-to)); |
| mask-radial-from-<color> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), <color> var(--tw-mask-radial-from), transparent var(--tw-mask-radial-to)); |
| mask-radial-from-(<custom-property>) | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(<custom-property>), transparent var(--tw-mask-radial-to)); |
| mask-radial-from-[<value>] | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black <value>, transparent var(--tw-mask-radial-to)); |
| mask-radial-to-<number> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent calc(var(--spacing * <number>))); |
| mask-radial-to-<percentage> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent <percentage>); |
| mask-radial-to-<color> | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), <color> var(--tw-mask-radial-to)); |
| mask-radial-to-(<custom-property>) | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent var(<custom-property>)); |
| mask-radial-to-[<value>] | mask-image: radial-gradient(var(--tw-mask-radial-shape) var(--tw-mask-radial-size) at var(--tw-mask-radial-position), black var(--tw-mask-radial-from), transparent <value>); |
| mask-circle | --tw-mask-radial-shape: circle; |
| mask-ellipse | --tw-mask-radial-shape: ellipse; |
| mask-radial-closest-corner | --tw-mask-radial-size: closest-corner; |
| mask-radial-closest-side | --tw-mask-radial-size: closest-side; |
| mask-radial-farthest-corner | --tw-mask-radial-size: farthest-corner; |
| mask-radial-farthest-side | --tw-mask-radial-size: farthest-side; |
| mask-radial-at-top-left | --tw-mask-radial-position: top left; |
| mask-radial-at-top | --tw-mask-radial-position: top; |
| mask-radial-at-top-right | --tw-mask-radial-position: top right; |
| mask-radial-at-left | --tw-mask-radial-position: left; |
| mask-radial-at-center | --tw-mask-radial-position:center; |
| mask-radial-at-right | --tw-mask-radial-position: right; |
| mask-radial-at-bottom-left | --tw-mask-radial-position: bottom left; |
| mask-radial-at-bottom | --tw-mask-radial-position: bottom; |
| mask-radial-at-bottom-right | --tw-mask-radial-position: bottom right; |
| mask-conic-<number> | mask-image: conic-gradient(from <number>deg, black var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to)); |
| -mask-conic-<number> | mask-image: conic-gradient(from calc(<number>deg * -1), black var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to)); |
| mask-conic-from-<number> | mask-image: conic-gradient(from var(--tw-mask-conic-position), black calc(var(--spacing * <number>)), transparent var(--tw-mask-conic-to)); |
| mask-conic-from-<percentage> | mask-image: conic-gradient(from var(--tw-mask-conic-position), black <percentage>, transparent var(--tw-mask-conic-to)); |
| mask-conic-from-<color> | mask-image: conic-gradient(from var(--tw-mask-conic-position), <color> var(--tw-mask-conic-from), transparent var(--tw-mask-conic-to)); |
| mask-conic-from-(<custom-property>) | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(<custom-property>), transparent var(--tw-mask-conic-to)); |
| mask-conic-from-[<value>] | mask-image: conic-gradient(from var(--tw-mask-conic-position), black <value>, transparent var(--tw-mask-conic-to)); |
| mask-conic-to-<number> | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent calc(var(--spacing * <number>)); |
| mask-conic-to-<percentage> | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent <percentage>); |
| mask-conic-to-<color> | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), <color> var(--tw-mask-conic-to); |
| mask-conic-to-(<custom-property>) | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent var(<custom-property>); |
| mask-conic-to-[<value>] | mask-image: conic-gradient(from var(--tw-mask-conic-position), black var(--tw-mask-conic-from), transparent <value>); |

[Documentation](https://tailwindcss.com/docs/mask-image)

---

## mask-mode

Utilities for controlling an element's mask mode.

### Classes

| Class | Styles |
| --- | --- |
| mask-alpha | mask-mode: alpha; |
| mask-luminance | mask-mode: luminance; |
| mask-match | mask-mode: match-source; |

[Documentation](https://tailwindcss.com/docs/mask-mode)

---

## mask-origin

Utilities for controlling how an element's mask image is positioned relative to borders, padding, and content.

### Classes

| Class | Styles |
| --- | --- |
| mask-origin-border | mask-origin: border-box; |
| mask-origin-padding | mask-origin: padding-box; |
| mask-origin-content | mask-origin: content-box; |
| mask-origin-fill | mask-origin: fill-box; |
| mask-origin-stroke | mask-origin: stroke-box; |
| mask-origin-view | mask-origin: view-box; |

[Documentation](https://tailwindcss.com/docs/mask-origin)

---

## mask-position

Utilities for controlling the position of an element's mask image.

### Classes

| Class | Styles |
| --- | --- |
| mask-top-left | mask-position: top left; |
| mask-top | mask-position: top; |
| mask-top-right | mask-position: top right; |
| mask-left | mask-position: left; |
| mask-center | mask-position: center; |
| mask-right | mask-position: right; |
| mask-bottom-left | mask-position: bottom left; |
| mask-bottom | mask-position: bottom; |
| mask-bottom-right | mask-position: bottom right; |
| mask-position-(<custom-property>) | mask-position: var(<custom-property>); |
| mask-position-[<value>] | mask-position: <value>; |

[Documentation](https://tailwindcss.com/docs/mask-position)

---

## mask-repeat

Utilities for controlling the repetition of an element's mask image.

### Classes

| Class | Styles |
| --- | --- |
| mask-repeat | mask-repeat: repeat; |
| mask-no-repeat | mask-repeat: no-repeat; |
| mask-repeat-x | mask-repeat: repeat-x; |
| mask-repeat-y | mask-repeat: repeat-y; |
| mask-repeat-space | mask-repeat: space; |
| mask-repeat-round | mask-repeat: round; |

[Documentation](https://tailwindcss.com/docs/mask-repeat)

---

## mask-size

Utilities for controlling the size of an element's mask image.

### Classes

| Class | Styles |
| --- | --- |
| mask-auto | mask-size: auto; |
| mask-cover | mask-size: cover; |
| mask-contain | mask-size: contain; |
| mask-size-(<custom-property>) | mask-size: var(<custom-property>); |
| mask-size-[<value>] | mask-size: <value>; |

[Documentation](https://tailwindcss.com/docs/mask-size)

---

## mask-type

Utilities for controlling how an SVG mask is interpreted.

### Classes

| Class | Styles |
| --- | --- |
| mask-type-alpha | mask-type: alpha; |
| mask-type-luminance | mask-type: luminance; |

[Documentation](https://tailwindcss.com/docs/mask-type)

---

