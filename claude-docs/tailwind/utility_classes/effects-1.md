# Effects - Part 1

This document contains Tailwind CSS classes for Effects.

## box-shadow

Utilities for controlling the box shadow of an element.

### Classes

| Class | Styles |
| --- | --- |
| shadow-2xs | box-shadow: var(--shadow-2xs); /* 0 1px rgb(0 0 0 / 0.05) */ |
| shadow-xs | box-shadow: var(--shadow-xs); /* 0 1px 2px 0 rgb(0 0 0 / 0.05) */ |
| shadow-sm | box-shadow: var(--shadow-sm); /* 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1) */ |
| shadow-md | box-shadow: var(--shadow-md); /* 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1) */ |
| shadow-lg | box-shadow: var(--shadow-lg); /* 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1) */ |
| shadow-xl | box-shadow: var(--shadow-xl); /* 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1) */ |
| shadow-2xl | box-shadow: var(--shadow-2xl); /* 0 25px 50px -12px rgb(0 0 0 / 0.25) */ |
| shadow-none | box-shadow: 0 0 #0000; |
| shadow-(<custom-property>) | box-shadow: var(<custom-property>); |
| shadow-(color:<custom-property>) | --tw-shadow-color: var(<custom-property>); |
| shadow-[<value>] | box-shadow: <value>; |
| shadow-inherit | --tw-shadow-color: inherit; |
| shadow-current | --tw-shadow-color: currentColor; |
| shadow-transparent | --tw-shadow-color: transparent; |
| shadow-black | --tw-shadow-color: var(--color-black); /* #000 */ |
| shadow-white | --tw-shadow-color: var(--color-white); /* #fff */ |
| shadow-red-50 | --tw-shadow-color: var(--color-red-50); |
| shadow-red-100 | --tw-shadow-color: var(--color-red-100); |
| shadow-red-200 | --tw-shadow-color: var(--color-red-200); |
| shadow-red-300 | --tw-shadow-color: var(--color-red-300); |
| shadow-red-400 | --tw-shadow-color: var(--color-red-400); |
| shadow-red-500 | --tw-shadow-color: var(--color-red-500); |
| shadow-red-600 | --tw-shadow-color: var(--color-red-600); |
| shadow-red-700 | --tw-shadow-color: var(--color-red-700); |
| shadow-red-800 | --tw-shadow-color: var(--color-red-800); |
| shadow-red-900 | --tw-shadow-color: var(--color-red-900); |
| shadow-red-950 | --tw-shadow-color: var(--color-red-950); |
| shadow-orange-50 | --tw-shadow-color: var(--color-orange-50); |
| shadow-orange-100 | --tw-shadow-color: var(--color-orange-100); |
| shadow-orange-200 | --tw-shadow-color: var(--color-orange-200); |
| shadow-orange-300 | --tw-shadow-color: var(--color-orange-300); |
| shadow-orange-400 | --tw-shadow-color: var(--color-orange-400); |
| shadow-orange-500 | --tw-shadow-color: var(--color-orange-500); |
| shadow-orange-600 | --tw-shadow-color: var(--color-orange-600); |
| shadow-orange-700 | --tw-shadow-color: var(--color-orange-700); |
| shadow-orange-800 | --tw-shadow-color: var(--color-orange-800); |
| shadow-orange-900 | --tw-shadow-color: var(--color-orange-900); |
| shadow-orange-950 | --tw-shadow-color: var(--color-orange-950); |
| shadow-amber-50 | --tw-shadow-color: var(--color-amber-50); |
| shadow-amber-100 | --tw-shadow-color: var(--color-amber-100); |
| shadow-amber-200 | --tw-shadow-color: var(--color-amber-200); |
| shadow-amber-300 | --tw-shadow-color: var(--color-amber-300); |
| shadow-amber-400 | --tw-shadow-color: var(--color-amber-400); |
| shadow-amber-500 | --tw-shadow-color: var(--color-amber-500); |
| shadow-amber-600 | --tw-shadow-color: var(--color-amber-600); |
| shadow-amber-700 | --tw-shadow-color: var(--color-amber-700); |
| shadow-amber-800 | --tw-shadow-color: var(--color-amber-800); |
| shadow-amber-900 | --tw-shadow-color: var(--color-amber-900); |
| shadow-amber-950 | --tw-shadow-color: var(--color-amber-950); |
| shadow-yellow-50 | --tw-shadow-color: var(--color-yellow-50); |
| shadow-yellow-100 | --tw-shadow-color: var(--color-yellow-100); |
| shadow-yellow-200 | --tw-shadow-color: var(--color-yellow-200); |
| shadow-yellow-300 | --tw-shadow-color: var(--color-yellow-300); |
| shadow-yellow-400 | --tw-shadow-color: var(--color-yellow-400); |
| shadow-yellow-500 | --tw-shadow-color: var(--color-yellow-500); |
| shadow-yellow-600 | --tw-shadow-color: var(--color-yellow-600); |
| shadow-yellow-700 | --tw-shadow-color: var(--color-yellow-700); |
| shadow-yellow-800 | --tw-shadow-color: var(--color-yellow-800); |
| shadow-yellow-900 | --tw-shadow-color: var(--color-yellow-900); |
| shadow-yellow-950 | --tw-shadow-color: var(--color-yellow-950); |
| shadow-lime-50 | --tw-shadow-color: var(--color-lime-50); |
| shadow-lime-100 | --tw-shadow-color: var(--color-lime-100); |
| shadow-lime-200 | --tw-shadow-color: var(--color-lime-200); |
| shadow-lime-300 | --tw-shadow-color: var(--color-lime-300); |
| shadow-lime-400 | --tw-shadow-color: var(--color-lime-400); |
| shadow-lime-500 | --tw-shadow-color: var(--color-lime-500); |
| shadow-lime-600 | --tw-shadow-color: var(--color-lime-600); |
| shadow-lime-700 | --tw-shadow-color: var(--color-lime-700); |
| shadow-lime-800 | --tw-shadow-color: var(--color-lime-800); |
| shadow-lime-900 | --tw-shadow-color: var(--color-lime-900); |
| shadow-lime-950 | --tw-shadow-color: var(--color-lime-950); |
| shadow-green-50 | --tw-shadow-color: var(--color-green-50); |
| shadow-green-100 | --tw-shadow-color: var(--color-green-100); |
| shadow-green-200 | --tw-shadow-color: var(--color-green-200); |
| shadow-green-300 | --tw-shadow-color: var(--color-green-300); |
| shadow-green-400 | --tw-shadow-color: var(--color-green-400); |
| shadow-green-500 | --tw-shadow-color: var(--color-green-500); |
| shadow-green-600 | --tw-shadow-color: var(--color-green-600); |
| shadow-green-700 | --tw-shadow-color: var(--color-green-700); |
| shadow-green-800 | --tw-shadow-color: var(--color-green-800); |
| shadow-green-900 | --tw-shadow-color: var(--color-green-900); |
| shadow-green-950 | --tw-shadow-color: var(--color-green-950); |
| shadow-emerald-50 | --tw-shadow-color: var(--color-emerald-50); |
| shadow-emerald-100 | --tw-shadow-color: var(--color-emerald-100); |
| shadow-emerald-200 | --tw-shadow-color: var(--color-emerald-200); |
| shadow-emerald-300 | --tw-shadow-color: var(--color-emerald-300); |
| shadow-emerald-400 | --tw-shadow-color: var(--color-emerald-400); |
| shadow-emerald-500 | --tw-shadow-color: var(--color-emerald-500); |
| shadow-emerald-600 | --tw-shadow-color: var(--color-emerald-600); |
| shadow-emerald-700 | --tw-shadow-color: var(--color-emerald-700); |
| shadow-emerald-800 | --tw-shadow-color: var(--color-emerald-800); |
| shadow-emerald-900 | --tw-shadow-color: var(--color-emerald-900); |
| shadow-emerald-950 | --tw-shadow-color: var(--color-emerald-950); |
| shadow-teal-50 | --tw-shadow-color: var(--color-teal-50); |
| shadow-teal-100 | --tw-shadow-color: var(--color-teal-100); |
| shadow-teal-200 | --tw-shadow-color: var(--color-teal-200); |
| shadow-teal-300 | --tw-shadow-color: var(--color-teal-300); |
| shadow-teal-400 | --tw-shadow-color: var(--color-teal-400); |
| shadow-teal-500 | --tw-shadow-color: var(--color-teal-500); |
| shadow-teal-600 | --tw-shadow-color: var(--color-teal-600); |
| shadow-teal-700 | --tw-shadow-color: var(--color-teal-700); |
| shadow-teal-800 | --tw-shadow-color: var(--color-teal-800); |
| shadow-teal-900 | --tw-shadow-color: var(--color-teal-900); |
| shadow-teal-950 | --tw-shadow-color: var(--color-teal-950); |
| shadow-cyan-50 | --tw-shadow-color: var(--color-cyan-50); |
| shadow-cyan-100 | --tw-shadow-color: var(--color-cyan-100); |
| shadow-cyan-200 | --tw-shadow-color: var(--color-cyan-200); |
| shadow-cyan-300 | --tw-shadow-color: var(--color-cyan-300); |
| shadow-cyan-400 | --tw-shadow-color: var(--color-cyan-400); |
| shadow-cyan-500 | --tw-shadow-color: var(--color-cyan-500); |
| shadow-cyan-600 | --tw-shadow-color: var(--color-cyan-600); |
| shadow-cyan-700 | --tw-shadow-color: var(--color-cyan-700); |
| shadow-cyan-800 | --tw-shadow-color: var(--color-cyan-800); |
| shadow-cyan-900 | --tw-shadow-color: var(--color-cyan-900); |
| shadow-cyan-950 | --tw-shadow-color: var(--color-cyan-950); |
| shadow-sky-50 | --tw-shadow-color: var(--color-sky-50); |
| shadow-sky-100 | --tw-shadow-color: var(--color-sky-100); |
| shadow-sky-200 | --tw-shadow-color: var(--color-sky-200); |
| shadow-sky-300 | --tw-shadow-color: var(--color-sky-300); |
| shadow-sky-400 | --tw-shadow-color: var(--color-sky-400); |
| shadow-sky-500 | --tw-shadow-color: var(--color-sky-500); |
| shadow-sky-600 | --tw-shadow-color: var(--color-sky-600); |
| shadow-sky-700 | --tw-shadow-color: var(--color-sky-700); |
| shadow-sky-800 | --tw-shadow-color: var(--color-sky-800); |
| shadow-sky-900 | --tw-shadow-color: var(--color-sky-900); |
| shadow-sky-950 | --tw-shadow-color: var(--color-sky-950); |
| shadow-blue-50 | --tw-shadow-color: var(--color-blue-50); |
| shadow-blue-100 | --tw-shadow-color: var(--color-blue-100); |
| shadow-blue-200 | --tw-shadow-color: var(--color-blue-200); |
| shadow-blue-300 | --tw-shadow-color: var(--color-blue-300); |
| shadow-blue-400 | --tw-shadow-color: var(--color-blue-400); |
| shadow-blue-500 | --tw-shadow-color: var(--color-blue-500); |
| shadow-blue-600 | --tw-shadow-color: var(--color-blue-600); |
| shadow-blue-700 | --tw-shadow-color: var(--color-blue-700); |
| shadow-blue-800 | --tw-shadow-color: var(--color-blue-800); |
| shadow-blue-900 | --tw-shadow-color: var(--color-blue-900); |
| shadow-blue-950 | --tw-shadow-color: var(--color-blue-950); |
| shadow-indigo-50 | --tw-shadow-color: var(--color-indigo-50); |
| shadow-indigo-100 | --tw-shadow-color: var(--color-indigo-100); |
| shadow-indigo-200 | --tw-shadow-color: var(--color-indigo-200); |
| shadow-indigo-300 | --tw-shadow-color: var(--color-indigo-300); |
| shadow-indigo-400 | --tw-shadow-color: var(--color-indigo-400); |
| shadow-indigo-500 | --tw-shadow-color: var(--color-indigo-500); |
| shadow-indigo-600 | --tw-shadow-color: var(--color-indigo-600); |
| shadow-indigo-700 | --tw-shadow-color: var(--color-indigo-700); |
| shadow-indigo-800 | --tw-shadow-color: var(--color-indigo-800); |
| shadow-indigo-900 | --tw-shadow-color: var(--color-indigo-900); |
| shadow-indigo-950 | --tw-shadow-color: var(--color-indigo-950); |
| shadow-violet-50 | --tw-shadow-color: var(--color-violet-50); |
| shadow-violet-100 | --tw-shadow-color: var(--color-violet-100); |
| shadow-violet-200 | --tw-shadow-color: var(--color-violet-200); |
| shadow-violet-300 | --tw-shadow-color: var(--color-violet-300); |
| shadow-violet-400 | --tw-shadow-color: var(--color-violet-400); |
| shadow-violet-500 | --tw-shadow-color: var(--color-violet-500); |
| shadow-violet-600 | --tw-shadow-color: var(--color-violet-600); |
| shadow-violet-700 | --tw-shadow-color: var(--color-violet-700); |
| shadow-violet-800 | --tw-shadow-color: var(--color-violet-800); |
| shadow-violet-900 | --tw-shadow-color: var(--color-violet-900); |
| shadow-violet-950 | --tw-shadow-color: var(--color-violet-950); |
| shadow-purple-50 | --tw-shadow-color: var(--color-purple-50); |
| shadow-purple-100 | --tw-shadow-color: var(--color-purple-100); |
| shadow-purple-200 | --tw-shadow-color: var(--color-purple-200); |
| shadow-purple-300 | --tw-shadow-color: var(--color-purple-300); |
| shadow-purple-400 | --tw-shadow-color: var(--color-purple-400); |
| shadow-purple-500 | --tw-shadow-color: var(--color-purple-500); |
| shadow-purple-600 | --tw-shadow-color: var(--color-purple-600); |
| shadow-purple-700 | --tw-shadow-color: var(--color-purple-700); |
| shadow-purple-800 | --tw-shadow-color: var(--color-purple-800); |
| shadow-purple-900 | --tw-shadow-color: var(--color-purple-900); |
| shadow-purple-950 | --tw-shadow-color: var(--color-purple-950); |
| shadow-fuchsia-50 | --tw-shadow-color: var(--color-fuchsia-50); |
| shadow-fuchsia-100 | --tw-shadow-color: var(--color-fuchsia-100); |
| shadow-fuchsia-200 | --tw-shadow-color: var(--color-fuchsia-200); |
| shadow-fuchsia-300 | --tw-shadow-color: var(--color-fuchsia-300); |
| shadow-fuchsia-400 | --tw-shadow-color: var(--color-fuchsia-400); |
| shadow-fuchsia-500 | --tw-shadow-color: var(--color-fuchsia-500); |
| shadow-fuchsia-600 | --tw-shadow-color: var(--color-fuchsia-600); |
| shadow-fuchsia-700 | --tw-shadow-color: var(--color-fuchsia-700); |
| shadow-fuchsia-800 | --tw-shadow-color: var(--color-fuchsia-800); |
| shadow-fuchsia-900 | --tw-shadow-color: var(--color-fuchsia-900); |
| shadow-fuchsia-950 | --tw-shadow-color: var(--color-fuchsia-950); |
| shadow-pink-50 | --tw-shadow-color: var(--color-pink-50); |
| shadow-pink-100 | --tw-shadow-color: var(--color-pink-100); |
| shadow-pink-200 | --tw-shadow-color: var(--color-pink-200); |
| shadow-pink-300 | --tw-shadow-color: var(--color-pink-300); |
| shadow-pink-400 | --tw-shadow-color: var(--color-pink-400); |
| shadow-pink-500 | --tw-shadow-color: var(--color-pink-500); |
| shadow-pink-600 | --tw-shadow-color: var(--color-pink-600); |
| shadow-pink-700 | --tw-shadow-color: var(--color-pink-700); |
| shadow-pink-800 | --tw-shadow-color: var(--color-pink-800); |
| shadow-pink-900 | --tw-shadow-color: var(--color-pink-900); |
| shadow-pink-950 | --tw-shadow-color: var(--color-pink-950); |
| shadow-rose-50 | --tw-shadow-color: var(--color-rose-50); |
| shadow-rose-100 | --tw-shadow-color: var(--color-rose-100); |
| shadow-rose-200 | --tw-shadow-color: var(--color-rose-200); |
| shadow-rose-300 | --tw-shadow-color: var(--color-rose-300); |
| shadow-rose-400 | --tw-shadow-color: var(--color-rose-400); |
| shadow-rose-500 | --tw-shadow-color: var(--color-rose-500); |
| shadow-rose-600 | --tw-shadow-color: var(--color-rose-600); |
| shadow-rose-700 | --tw-shadow-color: var(--color-rose-700); |
| shadow-rose-800 | --tw-shadow-color: var(--color-rose-800); |
| shadow-rose-900 | --tw-shadow-color: var(--color-rose-900); |
| shadow-rose-950 | --tw-shadow-color: var(--color-rose-950); |
| shadow-slate-50 | --tw-shadow-color: var(--color-slate-50); |
| shadow-slate-100 | --tw-shadow-color: var(--color-slate-100); |
| shadow-slate-200 | --tw-shadow-color: var(--color-slate-200); |
| shadow-slate-300 | --tw-shadow-color: var(--color-slate-300); |
| shadow-slate-400 | --tw-shadow-color: var(--color-slate-400); |
| shadow-slate-500 | --tw-shadow-color: var(--color-slate-500); |
| shadow-slate-600 | --tw-shadow-color: var(--color-slate-600); |
| shadow-slate-700 | --tw-shadow-color: var(--color-slate-700); |
| shadow-slate-800 | --tw-shadow-color: var(--color-slate-800); |
| shadow-slate-900 | --tw-shadow-color: var(--color-slate-900); |
| shadow-slate-950 | --tw-shadow-color: var(--color-slate-950); |
| shadow-gray-50 | --tw-shadow-color: var(--color-gray-50); |
| shadow-gray-100 | --tw-shadow-color: var(--color-gray-100); |
| shadow-gray-200 | --tw-shadow-color: var(--color-gray-200); |
| shadow-gray-300 | --tw-shadow-color: var(--color-gray-300); |
| shadow-gray-400 | --tw-shadow-color: var(--color-gray-400); |
| shadow-gray-500 | --tw-shadow-color: var(--color-gray-500); |
| shadow-gray-600 | --tw-shadow-color: var(--color-gray-600); |
| shadow-gray-700 | --tw-shadow-color: var(--color-gray-700); |
| shadow-gray-800 | --tw-shadow-color: var(--color-gray-800); |
| shadow-gray-900 | --tw-shadow-color: var(--color-gray-900); |
| shadow-gray-950 | --tw-shadow-color: var(--color-gray-950); |
| shadow-zinc-50 | --tw-shadow-color: var(--color-zinc-50); |
| shadow-zinc-100 | --tw-shadow-color: var(--color-zinc-100); |
| shadow-zinc-200 | --tw-shadow-color: var(--color-zinc-200); |
| shadow-zinc-300 | --tw-shadow-color: var(--color-zinc-300); |
| shadow-zinc-400 | --tw-shadow-color: var(--color-zinc-400); |
| shadow-zinc-500 | --tw-shadow-color: var(--color-zinc-500); |
| shadow-zinc-600 | --tw-shadow-color: var(--color-zinc-600); |
| shadow-zinc-700 | --tw-shadow-color: var(--color-zinc-700); |
| shadow-zinc-800 | --tw-shadow-color: var(--color-zinc-800); |
| shadow-zinc-900 | --tw-shadow-color: var(--color-zinc-900); |
| shadow-zinc-950 | --tw-shadow-color: var(--color-zinc-950); |
| shadow-neutral-50 | --tw-shadow-color: var(--color-neutral-50); |
| shadow-neutral-100 | --tw-shadow-color: var(--color-neutral-100); |
| shadow-neutral-200 | --tw-shadow-color: var(--color-neutral-200); |
| shadow-neutral-300 | --tw-shadow-color: var(--color-neutral-300); |
| shadow-neutral-400 | --tw-shadow-color: var(--color-neutral-400); |
| shadow-neutral-500 | --tw-shadow-color: var(--color-neutral-500); |
| shadow-neutral-600 | --tw-shadow-color: var(--color-neutral-600); |
| shadow-neutral-700 | --tw-shadow-color: var(--color-neutral-700); |
| shadow-neutral-800 | --tw-shadow-color: var(--color-neutral-800); |
| shadow-neutral-900 | --tw-shadow-color: var(--color-neutral-900); |
| shadow-neutral-950 | --tw-shadow-color: var(--color-neutral-950); |
| shadow-stone-50 | --tw-shadow-color: var(--color-stone-50); |
| shadow-stone-100 | --tw-shadow-color: var(--color-stone-100); |
| shadow-stone-200 | --tw-shadow-color: var(--color-stone-200); |
| shadow-stone-300 | --tw-shadow-color: var(--color-stone-300); |
| shadow-stone-400 | --tw-shadow-color: var(--color-stone-400); |
| shadow-stone-500 | --tw-shadow-color: var(--color-stone-500); |
| shadow-stone-600 | --tw-shadow-color: var(--color-stone-600); |
| shadow-stone-700 | --tw-shadow-color: var(--color-stone-700); |
| shadow-stone-800 | --tw-shadow-color: var(--color-stone-800); |
| shadow-stone-900 | --tw-shadow-color: var(--color-stone-900); |
| shadow-stone-950 | --tw-shadow-color: var(--color-stone-950); |

[Documentation](https://tailwindcss.com/docs/box-shadow)

---

