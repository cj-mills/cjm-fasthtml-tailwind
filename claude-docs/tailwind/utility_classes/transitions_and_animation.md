# Transitions & Animation

This document contains Tailwind CSS classes for Transitions & Animation.

## transition-property

Utilities for controlling which CSS properties transition.

### Classes

| Class | Styles |
| --- | --- |
| transition | transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to, opacity, box-shadow, transform, translate, scale, rotate, filter, -webkit-backdrop-filter, backdrop-filter;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-all | transition-property: all;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-colors | transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, --tw-gradient-from, --tw-gradient-via, --tw-gradient-to;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-opacity | transition-property: opacity;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-shadow | transition-property: box-shadow;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-transform | transition-property: transform, translate, scale, rotate;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-none | transition-property: none; |
| transition-(<custom-property>) | transition-property: var(<br><custom-property><br>);<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |
| transition-[<value>] | transition-property: <br><value><br>;<br>transition-timing-function: var(--default-transition-timing-function); <br>/* cubic-bezier(0.4, 0, 0.2, 1) */<br><br>transition-duration: var(--default-transition-duration); <br>/* 150ms */ |

[Documentation](https://tailwindcss.com/docs/transition-property)

---

## transition-behavior

Utilities to control the behavior of CSS transitions.

### Classes

| Class | Styles |
| --- | --- |
| transition-normal | transition-behavior: normal; |
| transition-discrete | transition-behavior: allow-discrete; |

[Documentation](https://tailwindcss.com/docs/transition-behavior)

---

## transition-duration

Utilities for controlling the duration of CSS transitions.

### Classes

| Class | Styles |
| --- | --- |
| duration-<number> | transition-duration: <number>ms; |
| duration-initial | transition-duration: initial; |
| duration-(<custom-property>) | transition-duration: var(<custom-property>); |
| duration-[<value>] | transition-duration: <value>; |

[Documentation](https://tailwindcss.com/docs/transition-duration)

---

## transition-timing-function

Utilities for controlling the easing of CSS transitions.

### Classes

| Class | Styles |
| --- | --- |
| ease-linear | transition-timing-function: linear; |
| ease-in | transition-timing-function: var(--ease-in); /* cubic-bezier(0.4, 0, 1, 1) */ |
| ease-out | transition-timing-function: var(--ease-out); /* cubic-bezier(0, 0, 0.2, 1) */ |
| ease-in-out | transition-timing-function: var(--ease-in-out); /* cubic-bezier(0.4, 0, 0.2, 1) */ |
| ease-initial | transition-timing-function: initial; |
| ease-(<custom-property>) | transition-timing-function: var(<custom-property>); |
| ease-[<value>] | transition-timing-function: <value>; |

[Documentation](https://tailwindcss.com/docs/transition-timing-function)

---

## transition-delay

Utilities for controlling the delay of CSS transitions.

### Classes

| Class | Styles |
| --- | --- |
| delay-<number> | transition-delay: <number>ms; |
| delay-(<custom-property>) | transition-delay: var(<custom-property>); |
| delay-[<value>] | transition-delay: <value>; |

[Documentation](https://tailwindcss.com/docs/transition-delay)

---

## animation

Utilities for animating elements with CSS animations.

### Classes

| Class | Styles |
| --- | --- |
| animate-spin | animation: var(--animate-spin); <br>/* spin 1s linear infinite */<br><br><br>@keyframes spin {<br>  to {<br>    transform: rotate(360deg);<br>  }<br>} |
| animate-ping | animation: var(--animate-ping); <br>/* ping 1s cubic-bezier(0, 0, 0.2, 1) infinite */<br><br><br>@keyframes ping {<br>  75%, 100% {<br>    transform: scale(2);<br>    opacity: 0;<br>  }<br>} |
| animate-pulse | animation: var(--animate-pulse); <br>/* pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite */<br><br><br>@keyframes pulse {<br>  50% {<br>    opacity: 0.5;<br>  }<br>} |
| animate-bounce | animation: var(--animate-bounce); <br>/* bounce 1s infinite */<br><br><br>@keyframes bounce {<br>  0%, 100% {<br>    transform: translateY(-25%);<br>    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);<br>  }<br>  50% {<br>    transform: none;<br>    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);<br>  }<br>} |
| animate-none | animation: none; |
| animate-(<custom-property>) | animation: var(<custom-property>); |
| animate-[<value>] | animation: <value>; |

[Documentation](https://tailwindcss.com/docs/animation)

---

