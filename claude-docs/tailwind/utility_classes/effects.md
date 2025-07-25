# Effects

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
| shadow-red-50 | --tw-shadow-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */ |
| shadow-red-100 | --tw-shadow-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */ |
| shadow-red-200 | --tw-shadow-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */ |
| shadow-red-300 | --tw-shadow-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */ |
| shadow-red-400 | --tw-shadow-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */ |
| shadow-red-500 | --tw-shadow-color: var(--color-red-500); /* oklch(63.7% 0.237 25.331) */ |
| shadow-red-600 | --tw-shadow-color: var(--color-red-600); /* oklch(57.7% 0.245 27.325) */ |
| shadow-red-700 | --tw-shadow-color: var(--color-red-700); /* oklch(50.5% 0.213 27.518) */ |
| shadow-red-800 | --tw-shadow-color: var(--color-red-800); /* oklch(44.4% 0.177 26.899) */ |
| shadow-red-900 | --tw-shadow-color: var(--color-red-900); /* oklch(39.6% 0.141 25.723) */ |
| shadow-red-950 | --tw-shadow-color: var(--color-red-950); /* oklch(25.8% 0.092 26.042) */ |
| shadow-orange-50 | --tw-shadow-color: var(--color-orange-50); /* oklch(98% 0.016 73.684) */ |
| shadow-orange-100 | --tw-shadow-color: var(--color-orange-100); /* oklch(95.4% 0.038 75.164) */ |
| shadow-orange-200 | --tw-shadow-color: var(--color-orange-200); /* oklch(90.1% 0.076 70.697) */ |
| shadow-orange-300 | --tw-shadow-color: var(--color-orange-300); /* oklch(83.7% 0.128 66.29) */ |
| shadow-orange-400 | --tw-shadow-color: var(--color-orange-400); /* oklch(75% 0.183 55.934) */ |
| shadow-orange-500 | --tw-shadow-color: var(--color-orange-500); /* oklch(70.5% 0.213 47.604) */ |
| shadow-orange-600 | --tw-shadow-color: var(--color-orange-600); /* oklch(64.6% 0.222 41.116) */ |
| shadow-orange-700 | --tw-shadow-color: var(--color-orange-700); /* oklch(55.3% 0.195 38.402) */ |
| shadow-orange-800 | --tw-shadow-color: var(--color-orange-800); /* oklch(47% 0.157 37.304) */ |
| shadow-orange-900 | --tw-shadow-color: var(--color-orange-900); /* oklch(40.8% 0.123 38.172) */ |
| shadow-orange-950 | --tw-shadow-color: var(--color-orange-950); /* oklch(26.6% 0.079 36.259) */ |
| shadow-amber-50 | --tw-shadow-color: var(--color-amber-50); /* oklch(98.7% 0.022 95.277) */ |
| shadow-amber-100 | --tw-shadow-color: var(--color-amber-100); /* oklch(96.2% 0.059 95.617) */ |
| shadow-amber-200 | --tw-shadow-color: var(--color-amber-200); /* oklch(92.4% 0.12 95.746) */ |
| shadow-amber-300 | --tw-shadow-color: var(--color-amber-300); /* oklch(87.9% 0.169 91.605) */ |
| shadow-amber-400 | --tw-shadow-color: var(--color-amber-400); /* oklch(82.8% 0.189 84.429) */ |
| shadow-amber-500 | --tw-shadow-color: var(--color-amber-500); /* oklch(76.9% 0.188 70.08) */ |
| shadow-amber-600 | --tw-shadow-color: var(--color-amber-600); /* oklch(66.6% 0.179 58.318) */ |
| shadow-amber-700 | --tw-shadow-color: var(--color-amber-700); /* oklch(55.5% 0.163 48.998) */ |
| shadow-amber-800 | --tw-shadow-color: var(--color-amber-800); /* oklch(47.3% 0.137 46.201) */ |
| shadow-amber-900 | --tw-shadow-color: var(--color-amber-900); /* oklch(41.4% 0.112 45.904) */ |
| shadow-amber-950 | --tw-shadow-color: var(--color-amber-950); /* oklch(27.9% 0.077 45.635) */ |
| shadow-yellow-50 | --tw-shadow-color: var(--color-yellow-50); /* oklch(98.7% 0.026 102.212) */ |
| shadow-yellow-100 | --tw-shadow-color: var(--color-yellow-100); /* oklch(97.3% 0.071 103.193) */ |
| shadow-yellow-200 | --tw-shadow-color: var(--color-yellow-200); /* oklch(94.5% 0.129 101.54) */ |
| shadow-yellow-300 | --tw-shadow-color: var(--color-yellow-300); /* oklch(90.5% 0.182 98.111) */ |
| shadow-yellow-400 | --tw-shadow-color: var(--color-yellow-400); /* oklch(85.2% 0.199 91.936) */ |
| shadow-yellow-500 | --tw-shadow-color: var(--color-yellow-500); /* oklch(79.5% 0.184 86.047) */ |
| shadow-yellow-600 | --tw-shadow-color: var(--color-yellow-600); /* oklch(68.1% 0.162 75.834) */ |
| shadow-yellow-700 | --tw-shadow-color: var(--color-yellow-700); /* oklch(55.4% 0.135 66.442) */ |
| shadow-yellow-800 | --tw-shadow-color: var(--color-yellow-800); /* oklch(47.6% 0.114 61.907) */ |
| shadow-yellow-900 | --tw-shadow-color: var(--color-yellow-900); /* oklch(42.1% 0.095 57.708) */ |
| shadow-yellow-950 | --tw-shadow-color: var(--color-yellow-950); /* oklch(28.6% 0.066 53.813) */ |
| shadow-lime-50 | --tw-shadow-color: var(--color-lime-50); /* oklch(98.6% 0.031 120.757) */ |
| shadow-lime-100 | --tw-shadow-color: var(--color-lime-100); /* oklch(96.7% 0.067 122.328) */ |
| shadow-lime-200 | --tw-shadow-color: var(--color-lime-200); /* oklch(93.8% 0.127 124.321) */ |
| shadow-lime-300 | --tw-shadow-color: var(--color-lime-300); /* oklch(89.7% 0.196 126.665) */ |
| shadow-lime-400 | --tw-shadow-color: var(--color-lime-400); /* oklch(84.1% 0.238 128.85) */ |
| shadow-lime-500 | --tw-shadow-color: var(--color-lime-500); /* oklch(76.8% 0.233 130.85) */ |
| shadow-lime-600 | --tw-shadow-color: var(--color-lime-600); /* oklch(64.8% 0.2 131.684) */ |
| shadow-lime-700 | --tw-shadow-color: var(--color-lime-700); /* oklch(53.2% 0.157 131.589) */ |
| shadow-lime-800 | --tw-shadow-color: var(--color-lime-800); /* oklch(45.3% 0.124 130.933) */ |
| shadow-lime-900 | --tw-shadow-color: var(--color-lime-900); /* oklch(40.5% 0.101 131.063) */ |
| shadow-lime-950 | --tw-shadow-color: var(--color-lime-950); /* oklch(27.4% 0.072 132.109) */ |
| shadow-green-50 | --tw-shadow-color: var(--color-green-50); /* oklch(98.2% 0.018 155.826) */ |
| shadow-green-100 | --tw-shadow-color: var(--color-green-100); /* oklch(96.2% 0.044 156.743) */ |
| shadow-green-200 | --tw-shadow-color: var(--color-green-200); /* oklch(92.5% 0.084 155.995) */ |
| shadow-green-300 | --tw-shadow-color: var(--color-green-300); /* oklch(87.1% 0.15 154.449) */ |
| shadow-green-400 | --tw-shadow-color: var(--color-green-400); /* oklch(79.2% 0.209 151.711) */ |
| shadow-green-500 | --tw-shadow-color: var(--color-green-500); /* oklch(72.3% 0.219 149.579) */ |
| shadow-green-600 | --tw-shadow-color: var(--color-green-600); /* oklch(62.7% 0.194 149.214) */ |
| shadow-green-700 | --tw-shadow-color: var(--color-green-700); /* oklch(52.7% 0.154 150.069) */ |
| shadow-green-800 | --tw-shadow-color: var(--color-green-800); /* oklch(44.8% 0.119 151.328) */ |
| shadow-green-900 | --tw-shadow-color: var(--color-green-900); /* oklch(39.3% 0.095 152.535) */ |
| shadow-green-950 | --tw-shadow-color: var(--color-green-950); /* oklch(26.6% 0.065 152.934) */ |
| shadow-emerald-50 | --tw-shadow-color: var(--color-emerald-50); /* oklch(97.9% 0.021 166.113) */ |
| shadow-emerald-100 | --tw-shadow-color: var(--color-emerald-100); /* oklch(95% 0.052 163.051) */ |
| shadow-emerald-200 | --tw-shadow-color: var(--color-emerald-200); /* oklch(90.5% 0.093 164.15) */ |
| shadow-emerald-300 | --tw-shadow-color: var(--color-emerald-300); /* oklch(84.5% 0.143 164.978) */ |
| shadow-emerald-400 | --tw-shadow-color: var(--color-emerald-400); /* oklch(76.5% 0.177 163.223) */ |
| shadow-emerald-500 | --tw-shadow-color: var(--color-emerald-500); /* oklch(69.6% 0.17 162.48) */ |
| shadow-emerald-600 | --tw-shadow-color: var(--color-emerald-600); /* oklch(59.6% 0.145 163.225) */ |
| shadow-emerald-700 | --tw-shadow-color: var(--color-emerald-700); /* oklch(50.8% 0.118 165.612) */ |
| shadow-emerald-800 | --tw-shadow-color: var(--color-emerald-800); /* oklch(43.2% 0.095 166.913) */ |
| shadow-emerald-900 | --tw-shadow-color: var(--color-emerald-900); /* oklch(37.8% 0.077 168.94) */ |
| shadow-emerald-950 | --tw-shadow-color: var(--color-emerald-950); /* oklch(26.2% 0.051 172.552) */ |
| shadow-teal-50 | --tw-shadow-color: var(--color-teal-50); /* oklch(98.4% 0.014 180.72) */ |
| shadow-teal-100 | --tw-shadow-color: var(--color-teal-100); /* oklch(95.3% 0.051 180.801) */ |
| shadow-teal-200 | --tw-shadow-color: var(--color-teal-200); /* oklch(91% 0.096 180.426) */ |
| shadow-teal-300 | --tw-shadow-color: var(--color-teal-300); /* oklch(85.5% 0.138 181.071) */ |
| shadow-teal-400 | --tw-shadow-color: var(--color-teal-400); /* oklch(77.7% 0.152 181.912) */ |
| shadow-teal-500 | --tw-shadow-color: var(--color-teal-500); /* oklch(70.4% 0.14 182.503) */ |
| shadow-teal-600 | --tw-shadow-color: var(--color-teal-600); /* oklch(60% 0.118 184.704) */ |
| shadow-teal-700 | --tw-shadow-color: var(--color-teal-700); /* oklch(51.1% 0.096 186.391) */ |
| shadow-teal-800 | --tw-shadow-color: var(--color-teal-800); /* oklch(43.7% 0.078 188.216) */ |
| shadow-teal-900 | --tw-shadow-color: var(--color-teal-900); /* oklch(38.6% 0.063 188.416) */ |
| shadow-teal-950 | --tw-shadow-color: var(--color-teal-950); /* oklch(27.7% 0.046 192.524) */ |
| shadow-cyan-50 | --tw-shadow-color: var(--color-cyan-50); /* oklch(98.4% 0.019 200.873) */ |
| shadow-cyan-100 | --tw-shadow-color: var(--color-cyan-100); /* oklch(95.6% 0.045 203.388) */ |
| shadow-cyan-200 | --tw-shadow-color: var(--color-cyan-200); /* oklch(91.7% 0.08 205.041) */ |
| shadow-cyan-300 | --tw-shadow-color: var(--color-cyan-300); /* oklch(86.5% 0.127 207.078) */ |
| shadow-cyan-400 | --tw-shadow-color: var(--color-cyan-400); /* oklch(78.9% 0.154 211.53) */ |
| shadow-cyan-500 | --tw-shadow-color: var(--color-cyan-500); /* oklch(71.5% 0.143 215.221) */ |
| shadow-cyan-600 | --tw-shadow-color: var(--color-cyan-600); /* oklch(60.9% 0.126 221.723) */ |
| shadow-cyan-700 | --tw-shadow-color: var(--color-cyan-700); /* oklch(52% 0.105 223.128) */ |
| shadow-cyan-800 | --tw-shadow-color: var(--color-cyan-800); /* oklch(45% 0.085 224.283) */ |
| shadow-cyan-900 | --tw-shadow-color: var(--color-cyan-900); /* oklch(39.8% 0.07 227.392) */ |
| shadow-cyan-950 | --tw-shadow-color: var(--color-cyan-950); /* oklch(30.2% 0.056 229.695) */ |
| shadow-sky-50 | --tw-shadow-color: var(--color-sky-50); /* oklch(97.7% 0.013 236.62) */ |
| shadow-sky-100 | --tw-shadow-color: var(--color-sky-100); /* oklch(95.1% 0.026 236.824) */ |
| shadow-sky-200 | --tw-shadow-color: var(--color-sky-200); /* oklch(90.1% 0.058 230.902) */ |
| shadow-sky-300 | --tw-shadow-color: var(--color-sky-300); /* oklch(82.8% 0.111 230.318) */ |
| shadow-sky-400 | --tw-shadow-color: var(--color-sky-400); /* oklch(74.6% 0.16 232.661) */ |
| shadow-sky-500 | --tw-shadow-color: var(--color-sky-500); /* oklch(68.5% 0.169 237.323) */ |
| shadow-sky-600 | --tw-shadow-color: var(--color-sky-600); /* oklch(58.8% 0.158 241.966) */ |
| shadow-sky-700 | --tw-shadow-color: var(--color-sky-700); /* oklch(50% 0.134 242.749) */ |
| shadow-sky-800 | --tw-shadow-color: var(--color-sky-800); /* oklch(44.3% 0.11 240.79) */ |
| shadow-sky-900 | --tw-shadow-color: var(--color-sky-900); /* oklch(39.1% 0.09 240.876) */ |
| shadow-sky-950 | --tw-shadow-color: var(--color-sky-950); /* oklch(29.3% 0.066 243.157) */ |
| shadow-blue-50 | --tw-shadow-color: var(--color-blue-50); /* oklch(97% 0.014 254.604) */ |
| shadow-blue-100 | --tw-shadow-color: var(--color-blue-100); /* oklch(93.2% 0.032 255.585) */ |
| shadow-blue-200 | --tw-shadow-color: var(--color-blue-200); /* oklch(88.2% 0.059 254.128) */ |
| shadow-blue-300 | --tw-shadow-color: var(--color-blue-300); /* oklch(80.9% 0.105 251.813) */ |
| shadow-blue-400 | --tw-shadow-color: var(--color-blue-400); /* oklch(70.7% 0.165 254.624) */ |
| shadow-blue-500 | --tw-shadow-color: var(--color-blue-500); /* oklch(62.3% 0.214 259.815) */ |
| shadow-blue-600 | --tw-shadow-color: var(--color-blue-600); /* oklch(54.6% 0.245 262.881) */ |
| shadow-blue-700 | --tw-shadow-color: var(--color-blue-700); /* oklch(48.8% 0.243 264.376) */ |
| shadow-blue-800 | --tw-shadow-color: var(--color-blue-800); /* oklch(42.4% 0.199 265.638) */ |
| shadow-blue-900 | --tw-shadow-color: var(--color-blue-900); /* oklch(37.9% 0.146 265.522) */ |
| shadow-blue-950 | --tw-shadow-color: var(--color-blue-950); /* oklch(28.2% 0.091 267.935) */ |
| shadow-indigo-50 | --tw-shadow-color: var(--color-indigo-50); /* oklch(96.2% 0.018 272.314) */ |
| shadow-indigo-100 | --tw-shadow-color: var(--color-indigo-100); /* oklch(93% 0.034 272.788) */ |
| shadow-indigo-200 | --tw-shadow-color: var(--color-indigo-200); /* oklch(87% 0.065 274.039) */ |
| shadow-indigo-300 | --tw-shadow-color: var(--color-indigo-300); /* oklch(78.5% 0.115 274.713) */ |
| shadow-indigo-400 | --tw-shadow-color: var(--color-indigo-400); /* oklch(67.3% 0.182 276.935) */ |
| shadow-indigo-500 | --tw-shadow-color: var(--color-indigo-500); /* oklch(58.5% 0.233 277.117) */ |
| shadow-indigo-600 | --tw-shadow-color: var(--color-indigo-600); /* oklch(51.1% 0.262 276.966) */ |
| shadow-indigo-700 | --tw-shadow-color: var(--color-indigo-700); /* oklch(45.7% 0.24 277.023) */ |
| shadow-indigo-800 | --tw-shadow-color: var(--color-indigo-800); /* oklch(39.8% 0.195 277.366) */ |
| shadow-indigo-900 | --tw-shadow-color: var(--color-indigo-900); /* oklch(35.9% 0.144 278.697) */ |
| shadow-indigo-950 | --tw-shadow-color: var(--color-indigo-950); /* oklch(25.7% 0.09 281.288) */ |
| shadow-violet-50 | --tw-shadow-color: var(--color-violet-50); /* oklch(96.9% 0.016 293.756) */ |
| shadow-violet-100 | --tw-shadow-color: var(--color-violet-100); /* oklch(94.3% 0.029 294.588) */ |
| shadow-violet-200 | --tw-shadow-color: var(--color-violet-200); /* oklch(89.4% 0.057 293.283) */ |
| shadow-violet-300 | --tw-shadow-color: var(--color-violet-300); /* oklch(81.1% 0.111 293.571) */ |
| shadow-violet-400 | --tw-shadow-color: var(--color-violet-400); /* oklch(70.2% 0.183 293.541) */ |
| shadow-violet-500 | --tw-shadow-color: var(--color-violet-500); /* oklch(60.6% 0.25 292.717) */ |
| shadow-violet-600 | --tw-shadow-color: var(--color-violet-600); /* oklch(54.1% 0.281 293.009) */ |
| shadow-violet-700 | --tw-shadow-color: var(--color-violet-700); /* oklch(49.1% 0.27 292.581) */ |
| shadow-violet-800 | --tw-shadow-color: var(--color-violet-800); /* oklch(43.2% 0.232 292.759) */ |
| shadow-violet-900 | --tw-shadow-color: var(--color-violet-900); /* oklch(38% 0.189 293.745) */ |
| shadow-violet-950 | --tw-shadow-color: var(--color-violet-950); /* oklch(28.3% 0.141 291.089) */ |
| shadow-purple-50 | --tw-shadow-color: var(--color-purple-50); /* oklch(97.7% 0.014 308.299) */ |
| shadow-purple-100 | --tw-shadow-color: var(--color-purple-100); /* oklch(94.6% 0.033 307.174) */ |
| shadow-purple-200 | --tw-shadow-color: var(--color-purple-200); /* oklch(90.2% 0.063 306.703) */ |
| shadow-purple-300 | --tw-shadow-color: var(--color-purple-300); /* oklch(82.7% 0.119 306.383) */ |
| shadow-purple-400 | --tw-shadow-color: var(--color-purple-400); /* oklch(71.4% 0.203 305.504) */ |
| shadow-purple-500 | --tw-shadow-color: var(--color-purple-500); /* oklch(62.7% 0.265 303.9) */ |
| shadow-purple-600 | --tw-shadow-color: var(--color-purple-600); /* oklch(55.8% 0.288 302.321) */ |
| shadow-purple-700 | --tw-shadow-color: var(--color-purple-700); /* oklch(49.6% 0.265 301.924) */ |
| shadow-purple-800 | --tw-shadow-color: var(--color-purple-800); /* oklch(43.8% 0.218 303.724) */ |
| shadow-purple-900 | --tw-shadow-color: var(--color-purple-900); /* oklch(38.1% 0.176 304.987) */ |
| shadow-purple-950 | --tw-shadow-color: var(--color-purple-950); /* oklch(29.1% 0.149 302.717) */ |
| shadow-fuchsia-50 | --tw-shadow-color: var(--color-fuchsia-50); /* oklch(97.7% 0.017 320.058) */ |
| shadow-fuchsia-100 | --tw-shadow-color: var(--color-fuchsia-100); /* oklch(95.2% 0.037 318.852) */ |
| shadow-fuchsia-200 | --tw-shadow-color: var(--color-fuchsia-200); /* oklch(90.3% 0.076 319.62) */ |
| shadow-fuchsia-300 | --tw-shadow-color: var(--color-fuchsia-300); /* oklch(83.3% 0.145 321.434) */ |
| shadow-fuchsia-400 | --tw-shadow-color: var(--color-fuchsia-400); /* oklch(74% 0.238 322.16) */ |
| shadow-fuchsia-500 | --tw-shadow-color: var(--color-fuchsia-500); /* oklch(66.7% 0.295 322.15) */ |
| shadow-fuchsia-600 | --tw-shadow-color: var(--color-fuchsia-600); /* oklch(59.1% 0.293 322.896) */ |
| shadow-fuchsia-700 | --tw-shadow-color: var(--color-fuchsia-700); /* oklch(51.8% 0.253 323.949) */ |
| shadow-fuchsia-800 | --tw-shadow-color: var(--color-fuchsia-800); /* oklch(45.2% 0.211 324.591) */ |
| shadow-fuchsia-900 | --tw-shadow-color: var(--color-fuchsia-900); /* oklch(40.1% 0.17 325.612) */ |
| shadow-fuchsia-950 | --tw-shadow-color: var(--color-fuchsia-950); /* oklch(29.3% 0.136 325.661) */ |
| shadow-pink-50 | --tw-shadow-color: var(--color-pink-50); /* oklch(97.1% 0.014 343.198) */ |
| shadow-pink-100 | --tw-shadow-color: var(--color-pink-100); /* oklch(94.8% 0.028 342.258) */ |
| shadow-pink-200 | --tw-shadow-color: var(--color-pink-200); /* oklch(89.9% 0.061 343.231) */ |
| shadow-pink-300 | --tw-shadow-color: var(--color-pink-300); /* oklch(82.3% 0.12 346.018) */ |
| shadow-pink-400 | --tw-shadow-color: var(--color-pink-400); /* oklch(71.8% 0.202 349.761) */ |
| shadow-pink-500 | --tw-shadow-color: var(--color-pink-500); /* oklch(65.6% 0.241 354.308) */ |
| shadow-pink-600 | --tw-shadow-color: var(--color-pink-600); /* oklch(59.2% 0.249 0.584) */ |
| shadow-pink-700 | --tw-shadow-color: var(--color-pink-700); /* oklch(52.5% 0.223 3.958) */ |
| shadow-pink-800 | --tw-shadow-color: var(--color-pink-800); /* oklch(45.9% 0.187 3.815) */ |
| shadow-pink-900 | --tw-shadow-color: var(--color-pink-900); /* oklch(40.8% 0.153 2.432) */ |
| shadow-pink-950 | --tw-shadow-color: var(--color-pink-950); /* oklch(28.4% 0.109 3.907) */ |
| shadow-rose-50 | --tw-shadow-color: var(--color-rose-50); /* oklch(96.9% 0.015 12.422) */ |
| shadow-rose-100 | --tw-shadow-color: var(--color-rose-100); /* oklch(94.1% 0.03 12.58) */ |
| shadow-rose-200 | --tw-shadow-color: var(--color-rose-200); /* oklch(89.2% 0.058 10.001) */ |
| shadow-rose-300 | --tw-shadow-color: var(--color-rose-300); /* oklch(81% 0.117 11.638) */ |
| shadow-rose-400 | --tw-shadow-color: var(--color-rose-400); /* oklch(71.2% 0.194 13.428) */ |
| shadow-rose-500 | --tw-shadow-color: var(--color-rose-500); /* oklch(64.5% 0.246 16.439) */ |
| shadow-rose-600 | --tw-shadow-color: var(--color-rose-600); /* oklch(58.6% 0.253 17.585) */ |
| shadow-rose-700 | --tw-shadow-color: var(--color-rose-700); /* oklch(51.4% 0.222 16.935) */ |
| shadow-rose-800 | --tw-shadow-color: var(--color-rose-800); /* oklch(45.5% 0.188 13.697) */ |
| shadow-rose-900 | --tw-shadow-color: var(--color-rose-900); /* oklch(41% 0.159 10.272) */ |
| shadow-rose-950 | --tw-shadow-color: var(--color-rose-950); /* oklch(27.1% 0.105 12.094) */ |
| shadow-slate-50 | --tw-shadow-color: var(--color-slate-50); /* oklch(98.4% 0.003 247.858) */ |
| shadow-slate-100 | --tw-shadow-color: var(--color-slate-100); /* oklch(96.8% 0.007 247.896) */ |
| shadow-slate-200 | --tw-shadow-color: var(--color-slate-200); /* oklch(92.9% 0.013 255.508) */ |
| shadow-slate-300 | --tw-shadow-color: var(--color-slate-300); /* oklch(86.9% 0.022 252.894) */ |
| shadow-slate-400 | --tw-shadow-color: var(--color-slate-400); /* oklch(70.4% 0.04 256.788) */ |
| shadow-slate-500 | --tw-shadow-color: var(--color-slate-500); /* oklch(55.4% 0.046 257.417) */ |
| shadow-slate-600 | --tw-shadow-color: var(--color-slate-600); /* oklch(44.6% 0.043 257.281) */ |
| shadow-slate-700 | --tw-shadow-color: var(--color-slate-700); /* oklch(37.2% 0.044 257.287) */ |
| shadow-slate-800 | --tw-shadow-color: var(--color-slate-800); /* oklch(27.9% 0.041 260.031) */ |
| shadow-slate-900 | --tw-shadow-color: var(--color-slate-900); /* oklch(20.8% 0.042 265.755) */ |
| shadow-slate-950 | --tw-shadow-color: var(--color-slate-950); /* oklch(12.9% 0.042 264.695) */ |
| shadow-gray-50 | --tw-shadow-color: var(--color-gray-50); /* oklch(98.5% 0.002 247.839) */ |
| shadow-gray-100 | --tw-shadow-color: var(--color-gray-100); /* oklch(96.7% 0.003 264.542) */ |
| shadow-gray-200 | --tw-shadow-color: var(--color-gray-200); /* oklch(92.8% 0.006 264.531) */ |
| shadow-gray-300 | --tw-shadow-color: var(--color-gray-300); /* oklch(87.2% 0.01 258.338) */ |
| shadow-gray-400 | --tw-shadow-color: var(--color-gray-400); /* oklch(70.7% 0.022 261.325) */ |
| shadow-gray-500 | --tw-shadow-color: var(--color-gray-500); /* oklch(55.1% 0.027 264.364) */ |
| shadow-gray-600 | --tw-shadow-color: var(--color-gray-600); /* oklch(44.6% 0.03 256.802) */ |
| shadow-gray-700 | --tw-shadow-color: var(--color-gray-700); /* oklch(37.3% 0.034 259.733) */ |
| shadow-gray-800 | --tw-shadow-color: var(--color-gray-800); /* oklch(27.8% 0.033 256.848) */ |
| shadow-gray-900 | --tw-shadow-color: var(--color-gray-900); /* oklch(21% 0.034 264.665) */ |
| shadow-gray-950 | --tw-shadow-color: var(--color-gray-950); /* oklch(13% 0.028 261.692) */ |
| shadow-zinc-50 | --tw-shadow-color: var(--color-zinc-50); /* oklch(98.5% 0 0) */ |
| shadow-zinc-100 | --tw-shadow-color: var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */ |
| shadow-zinc-200 | --tw-shadow-color: var(--color-zinc-200); /* oklch(92% 0.004 286.32) */ |
| shadow-zinc-300 | --tw-shadow-color: var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */ |
| shadow-zinc-400 | --tw-shadow-color: var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */ |
| shadow-zinc-500 | --tw-shadow-color: var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */ |
| shadow-zinc-600 | --tw-shadow-color: var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */ |
| shadow-zinc-700 | --tw-shadow-color: var(--color-zinc-700); /* oklch(37% 0.013 285.805) */ |
| shadow-zinc-800 | --tw-shadow-color: var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */ |
| shadow-zinc-900 | --tw-shadow-color: var(--color-zinc-900); /* oklch(21% 0.006 285.885) */ |
| shadow-zinc-950 | --tw-shadow-color: var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */ |
| shadow-neutral-50 | --tw-shadow-color: var(--color-neutral-50); /* oklch(98.5% 0 0) */ |
| shadow-neutral-100 | --tw-shadow-color: var(--color-neutral-100); /* oklch(97% 0 0) */ |
| shadow-neutral-200 | --tw-shadow-color: var(--color-neutral-200); /* oklch(92.2% 0 0) */ |
| shadow-neutral-300 | --tw-shadow-color: var(--color-neutral-300); /* oklch(87% 0 0) */ |
| shadow-neutral-400 | --tw-shadow-color: var(--color-neutral-400); /* oklch(70.8% 0 0) */ |
| shadow-neutral-500 | --tw-shadow-color: var(--color-neutral-500); /* oklch(55.6% 0 0) */ |
| shadow-neutral-600 | --tw-shadow-color: var(--color-neutral-600); /* oklch(43.9% 0 0) */ |
| shadow-neutral-700 | --tw-shadow-color: var(--color-neutral-700); /* oklch(37.1% 0 0) */ |
| shadow-neutral-800 | --tw-shadow-color: var(--color-neutral-800); /* oklch(26.9% 0 0) */ |
| shadow-neutral-900 | --tw-shadow-color: var(--color-neutral-900); /* oklch(20.5% 0 0) */ |
| shadow-neutral-950 | --tw-shadow-color: var(--color-neutral-950); /* oklch(14.5% 0 0) */ |
| shadow-stone-50 | --tw-shadow-color: var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */ |
| shadow-stone-100 | --tw-shadow-color: var(--color-stone-100); /* oklch(97% 0.001 106.424) */ |
| shadow-stone-200 | --tw-shadow-color: var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */ |
| shadow-stone-300 | --tw-shadow-color: var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */ |
| shadow-stone-400 | --tw-shadow-color: var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */ |
| shadow-stone-500 | --tw-shadow-color: var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */ |
| shadow-stone-600 | --tw-shadow-color: var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */ |
| shadow-stone-700 | --tw-shadow-color: var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */ |
| shadow-stone-800 | --tw-shadow-color: var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */ |
| shadow-stone-900 | --tw-shadow-color: var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */ |
| shadow-stone-950 | --tw-shadow-color: var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */ |
| inset-shadow-2xs | box-shadow: var(--inset-shadow-2xs); /* inset 0 1px rgb(0 0 0 / 0.05) */ |
| inset-shadow-xs | box-shadow: var(--inset-shadow-xs); /* inset 0 1px 1px rgb(0 0 0 / 0.05) */ |
| inset-shadow-sm | box-shadow: var(--inset-shadow-sm); /* inset 0 2px 4px rgb(0 0 0 / 0.05) */ |
| inset-shadow-none | box-shadow: inset 0 0 #0000; |
| inset-shadow-(<custom-property>) | box-shadow: var(<custom-property>); |
| inset-shadow-[<value>] | box-shadow: <value>; |
| inset-shadow-inherit | --tw-inset-shadow-color: inherit; |
| inset-shadow-current | --tw-inset-shadow-color: currentColor; |
| inset-shadow-transparent | --tw-inset-shadow-color: transparent; |
| inset-shadow-black | --tw-inset-shadow-color: var(--color-black); /* #000 */ |
| inset-shadow-white | --tw-inset-shadow-color: var(--color-white); /* #fff */ |
| inset-shadow-red-50 | --tw-inset-shadow-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */ |
| inset-shadow-red-100 | --tw-inset-shadow-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */ |
| inset-shadow-red-200 | --tw-inset-shadow-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */ |
| inset-shadow-red-300 | --tw-inset-shadow-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */ |
| inset-shadow-red-400 | --tw-inset-shadow-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */ |
| inset-shadow-red-500 | --tw-inset-shadow-color: var(--color-red-500); /* oklch(63.7% 0.237 25.331) */ |
| inset-shadow-red-600 | --tw-inset-shadow-color: var(--color-red-600); /* oklch(57.7% 0.245 27.325) */ |
| inset-shadow-red-700 | --tw-inset-shadow-color: var(--color-red-700); /* oklch(50.5% 0.213 27.518) */ |
| inset-shadow-red-800 | --tw-inset-shadow-color: var(--color-red-800); /* oklch(44.4% 0.177 26.899) */ |
| inset-shadow-red-900 | --tw-inset-shadow-color: var(--color-red-900); /* oklch(39.6% 0.141 25.723) */ |
| inset-shadow-red-950 | --tw-inset-shadow-color: var(--color-red-950); /* oklch(25.8% 0.092 26.042) */ |
| inset-shadow-orange-50 | --tw-inset-shadow-color: var(--color-orange-50); /* oklch(98% 0.016 73.684) */ |
| inset-shadow-orange-100 | --tw-inset-shadow-color: var(--color-orange-100); /* oklch(95.4% 0.038 75.164) */ |
| inset-shadow-orange-200 | --tw-inset-shadow-color: var(--color-orange-200); /* oklch(90.1% 0.076 70.697) */ |
| inset-shadow-orange-300 | --tw-inset-shadow-color: var(--color-orange-300); /* oklch(83.7% 0.128 66.29) */ |
| inset-shadow-orange-400 | --tw-inset-shadow-color: var(--color-orange-400); /* oklch(75% 0.183 55.934) */ |
| inset-shadow-orange-500 | --tw-inset-shadow-color: var(--color-orange-500); /* oklch(70.5% 0.213 47.604) */ |
| inset-shadow-orange-600 | --tw-inset-shadow-color: var(--color-orange-600); /* oklch(64.6% 0.222 41.116) */ |
| inset-shadow-orange-700 | --tw-inset-shadow-color: var(--color-orange-700); /* oklch(55.3% 0.195 38.402) */ |
| inset-shadow-orange-800 | --tw-inset-shadow-color: var(--color-orange-800); /* oklch(47% 0.157 37.304) */ |
| inset-shadow-orange-900 | --tw-inset-shadow-color: var(--color-orange-900); /* oklch(40.8% 0.123 38.172) */ |
| inset-shadow-orange-950 | --tw-inset-shadow-color: var(--color-orange-950); /* oklch(26.6% 0.079 36.259) */ |
| inset-shadow-amber-50 | --tw-inset-shadow-color: var(--color-amber-50); /* oklch(98.7% 0.022 95.277) */ |
| inset-shadow-amber-100 | --tw-inset-shadow-color: var(--color-amber-100); /* oklch(96.2% 0.059 95.617) */ |
| inset-shadow-amber-200 | --tw-inset-shadow-color: var(--color-amber-200); /* oklch(92.4% 0.12 95.746) */ |
| inset-shadow-amber-300 | --tw-inset-shadow-color: var(--color-amber-300); /* oklch(87.9% 0.169 91.605) */ |
| inset-shadow-amber-400 | --tw-inset-shadow-color: var(--color-amber-400); /* oklch(82.8% 0.189 84.429) */ |
| inset-shadow-amber-500 | --tw-inset-shadow-color: var(--color-amber-500); /* oklch(76.9% 0.188 70.08) */ |
| inset-shadow-amber-600 | --tw-inset-shadow-color: var(--color-amber-600); /* oklch(66.6% 0.179 58.318) */ |
| inset-shadow-amber-700 | --tw-inset-shadow-color: var(--color-amber-700); /* oklch(55.5% 0.163 48.998) */ |
| inset-shadow-amber-800 | --tw-inset-shadow-color: var(--color-amber-800); /* oklch(47.3% 0.137 46.201) */ |
| inset-shadow-amber-900 | --tw-inset-shadow-color: var(--color-amber-900); /* oklch(41.4% 0.112 45.904) */ |
| inset-shadow-amber-950 | --tw-inset-shadow-color: var(--color-amber-950); /* oklch(27.9% 0.077 45.635) */ |
| inset-shadow-yellow-50 | --tw-inset-shadow-color: var(--color-yellow-50); /* oklch(98.7% 0.026 102.212) */ |
| inset-shadow-yellow-100 | --tw-inset-shadow-color: var(--color-yellow-100); /* oklch(97.3% 0.071 103.193) */ |
| inset-shadow-yellow-200 | --tw-inset-shadow-color: var(--color-yellow-200); /* oklch(94.5% 0.129 101.54) */ |
| inset-shadow-yellow-300 | --tw-inset-shadow-color: var(--color-yellow-300); /* oklch(90.5% 0.182 98.111) */ |
| inset-shadow-yellow-400 | --tw-inset-shadow-color: var(--color-yellow-400); /* oklch(85.2% 0.199 91.936) */ |
| inset-shadow-yellow-500 | --tw-inset-shadow-color: var(--color-yellow-500); /* oklch(79.5% 0.184 86.047) */ |
| inset-shadow-yellow-600 | --tw-inset-shadow-color: var(--color-yellow-600); /* oklch(68.1% 0.162 75.834) */ |
| inset-shadow-yellow-700 | --tw-inset-shadow-color: var(--color-yellow-700); /* oklch(55.4% 0.135 66.442) */ |
| inset-shadow-yellow-800 | --tw-inset-shadow-color: var(--color-yellow-800); /* oklch(47.6% 0.114 61.907) */ |
| inset-shadow-yellow-900 | --tw-inset-shadow-color: var(--color-yellow-900); /* oklch(42.1% 0.095 57.708) */ |
| inset-shadow-yellow-950 | --tw-inset-shadow-color: var(--color-yellow-950); /* oklch(28.6% 0.066 53.813) */ |
| inset-shadow-lime-50 | --tw-inset-shadow-color: var(--color-lime-50); /* oklch(98.6% 0.031 120.757) */ |
| inset-shadow-lime-100 | --tw-inset-shadow-color: var(--color-lime-100); /* oklch(96.7% 0.067 122.328) */ |
| inset-shadow-lime-200 | --tw-inset-shadow-color: var(--color-lime-200); /* oklch(93.8% 0.127 124.321) */ |
| inset-shadow-lime-300 | --tw-inset-shadow-color: var(--color-lime-300); /* oklch(89.7% 0.196 126.665) */ |
| inset-shadow-lime-400 | --tw-inset-shadow-color: var(--color-lime-400); /* oklch(84.1% 0.238 128.85) */ |
| inset-shadow-lime-500 | --tw-inset-shadow-color: var(--color-lime-500); /* oklch(76.8% 0.233 130.85) */ |
| inset-shadow-lime-600 | --tw-inset-shadow-color: var(--color-lime-600); /* oklch(64.8% 0.2 131.684) */ |
| inset-shadow-lime-700 | --tw-inset-shadow-color: var(--color-lime-700); /* oklch(53.2% 0.157 131.589) */ |
| inset-shadow-lime-800 | --tw-inset-shadow-color: var(--color-lime-800); /* oklch(45.3% 0.124 130.933) */ |
| inset-shadow-lime-900 | --tw-inset-shadow-color: var(--color-lime-900); /* oklch(40.5% 0.101 131.063) */ |
| inset-shadow-lime-950 | --tw-inset-shadow-color: var(--color-lime-950); /* oklch(27.4% 0.072 132.109) */ |
| inset-shadow-green-50 | --tw-inset-shadow-color: var(--color-green-50); /* oklch(98.2% 0.018 155.826) */ |
| inset-shadow-green-100 | --tw-inset-shadow-color: var(--color-green-100); /* oklch(96.2% 0.044 156.743) */ |
| inset-shadow-green-200 | --tw-inset-shadow-color: var(--color-green-200); /* oklch(92.5% 0.084 155.995) */ |
| inset-shadow-green-300 | --tw-inset-shadow-color: var(--color-green-300); /* oklch(87.1% 0.15 154.449) */ |
| inset-shadow-green-400 | --tw-inset-shadow-color: var(--color-green-400); /* oklch(79.2% 0.209 151.711) */ |
| inset-shadow-green-500 | --tw-inset-shadow-color: var(--color-green-500); /* oklch(72.3% 0.219 149.579) */ |
| inset-shadow-green-600 | --tw-inset-shadow-color: var(--color-green-600); /* oklch(62.7% 0.194 149.214) */ |
| inset-shadow-green-700 | --tw-inset-shadow-color: var(--color-green-700); /* oklch(52.7% 0.154 150.069) */ |
| inset-shadow-green-800 | --tw-inset-shadow-color: var(--color-green-800); /* oklch(44.8% 0.119 151.328) */ |
| inset-shadow-green-900 | --tw-inset-shadow-color: var(--color-green-900); /* oklch(39.3% 0.095 152.535) */ |
| inset-shadow-green-950 | --tw-inset-shadow-color: var(--color-green-950); /* oklch(26.6% 0.065 152.934) */ |
| inset-shadow-emerald-50 | --tw-inset-shadow-color: var(--color-emerald-50); /* oklch(97.9% 0.021 166.113) */ |
| inset-shadow-emerald-100 | --tw-inset-shadow-color: var(--color-emerald-100); /* oklch(95% 0.052 163.051) */ |
| inset-shadow-emerald-200 | --tw-inset-shadow-color: var(--color-emerald-200); /* oklch(90.5% 0.093 164.15) */ |
| inset-shadow-emerald-300 | --tw-inset-shadow-color: var(--color-emerald-300); /* oklch(84.5% 0.143 164.978) */ |
| inset-shadow-emerald-400 | --tw-inset-shadow-color: var(--color-emerald-400); /* oklch(76.5% 0.177 163.223) */ |
| inset-shadow-emerald-500 | --tw-inset-shadow-color: var(--color-emerald-500); /* oklch(69.6% 0.17 162.48) */ |
| inset-shadow-emerald-600 | --tw-inset-shadow-color: var(--color-emerald-600); /* oklch(59.6% 0.145 163.225) */ |
| inset-shadow-emerald-700 | --tw-inset-shadow-color: var(--color-emerald-700); /* oklch(50.8% 0.118 165.612) */ |
| inset-shadow-emerald-800 | --tw-inset-shadow-color: var(--color-emerald-800); /* oklch(43.2% 0.095 166.913) */ |
| inset-shadow-emerald-900 | --tw-inset-shadow-color: var(--color-emerald-900); /* oklch(37.8% 0.077 168.94) */ |
| inset-shadow-emerald-950 | --tw-inset-shadow-color: var(--color-emerald-950); /* oklch(26.2% 0.051 172.552) */ |
| inset-shadow-teal-50 | --tw-inset-shadow-color: var(--color-teal-50); /* oklch(98.4% 0.014 180.72) */ |
| inset-shadow-teal-100 | --tw-inset-shadow-color: var(--color-teal-100); /* oklch(95.3% 0.051 180.801) */ |
| inset-shadow-teal-200 | --tw-inset-shadow-color: var(--color-teal-200); /* oklch(91% 0.096 180.426) */ |
| inset-shadow-teal-300 | --tw-inset-shadow-color: var(--color-teal-300); /* oklch(85.5% 0.138 181.071) */ |
| inset-shadow-teal-400 | --tw-inset-shadow-color: var(--color-teal-400); /* oklch(77.7% 0.152 181.912) */ |
| inset-shadow-teal-500 | --tw-inset-shadow-color: var(--color-teal-500); /* oklch(70.4% 0.14 182.503) */ |
| inset-shadow-teal-600 | --tw-inset-shadow-color: var(--color-teal-600); /* oklch(60% 0.118 184.704) */ |
| inset-shadow-teal-700 | --tw-inset-shadow-color: var(--color-teal-700); /* oklch(51.1% 0.096 186.391) */ |
| inset-shadow-teal-800 | --tw-inset-shadow-color: var(--color-teal-800); /* oklch(43.7% 0.078 188.216) */ |
| inset-shadow-teal-900 | --tw-inset-shadow-color: var(--color-teal-900); /* oklch(38.6% 0.063 188.416) */ |
| inset-shadow-teal-950 | --tw-inset-shadow-color: var(--color-teal-950); /* oklch(27.7% 0.046 192.524) */ |
| inset-shadow-cyan-50 | --tw-inset-shadow-color: var(--color-cyan-50); /* oklch(98.4% 0.019 200.873) */ |
| inset-shadow-cyan-100 | --tw-inset-shadow-color: var(--color-cyan-100); /* oklch(95.6% 0.045 203.388) */ |
| inset-shadow-cyan-200 | --tw-inset-shadow-color: var(--color-cyan-200); /* oklch(91.7% 0.08 205.041) */ |
| inset-shadow-cyan-300 | --tw-inset-shadow-color: var(--color-cyan-300); /* oklch(86.5% 0.127 207.078) */ |
| inset-shadow-cyan-400 | --tw-inset-shadow-color: var(--color-cyan-400); /* oklch(78.9% 0.154 211.53) */ |
| inset-shadow-cyan-500 | --tw-inset-shadow-color: var(--color-cyan-500); /* oklch(71.5% 0.143 215.221) */ |
| inset-shadow-cyan-600 | --tw-inset-shadow-color: var(--color-cyan-600); /* oklch(60.9% 0.126 221.723) */ |
| inset-shadow-cyan-700 | --tw-inset-shadow-color: var(--color-cyan-700); /* oklch(52% 0.105 223.128) */ |
| inset-shadow-cyan-800 | --tw-inset-shadow-color: var(--color-cyan-800); /* oklch(45% 0.085 224.283) */ |
| inset-shadow-cyan-900 | --tw-inset-shadow-color: var(--color-cyan-900); /* oklch(39.8% 0.07 227.392) */ |
| inset-shadow-cyan-950 | --tw-inset-shadow-color: var(--color-cyan-950); /* oklch(30.2% 0.056 229.695) */ |
| inset-shadow-sky-50 | --tw-inset-shadow-color: var(--color-sky-50); /* oklch(97.7% 0.013 236.62) */ |
| inset-shadow-sky-100 | --tw-inset-shadow-color: var(--color-sky-100); /* oklch(95.1% 0.026 236.824) */ |
| inset-shadow-sky-200 | --tw-inset-shadow-color: var(--color-sky-200); /* oklch(90.1% 0.058 230.902) */ |
| inset-shadow-sky-300 | --tw-inset-shadow-color: var(--color-sky-300); /* oklch(82.8% 0.111 230.318) */ |
| inset-shadow-sky-400 | --tw-inset-shadow-color: var(--color-sky-400); /* oklch(74.6% 0.16 232.661) */ |
| inset-shadow-sky-500 | --tw-inset-shadow-color: var(--color-sky-500); /* oklch(68.5% 0.169 237.323) */ |
| inset-shadow-sky-600 | --tw-inset-shadow-color: var(--color-sky-600); /* oklch(58.8% 0.158 241.966) */ |
| inset-shadow-sky-700 | --tw-inset-shadow-color: var(--color-sky-700); /* oklch(50% 0.134 242.749) */ |
| inset-shadow-sky-800 | --tw-inset-shadow-color: var(--color-sky-800); /* oklch(44.3% 0.11 240.79) */ |
| inset-shadow-sky-900 | --tw-inset-shadow-color: var(--color-sky-900); /* oklch(39.1% 0.09 240.876) */ |
| inset-shadow-sky-950 | --tw-inset-shadow-color: var(--color-sky-950); /* oklch(29.3% 0.066 243.157) */ |
| inset-shadow-blue-50 | --tw-inset-shadow-color: var(--color-blue-50); /* oklch(97% 0.014 254.604) */ |
| inset-shadow-blue-100 | --tw-inset-shadow-color: var(--color-blue-100); /* oklch(93.2% 0.032 255.585) */ |
| inset-shadow-blue-200 | --tw-inset-shadow-color: var(--color-blue-200); /* oklch(88.2% 0.059 254.128) */ |
| inset-shadow-blue-300 | --tw-inset-shadow-color: var(--color-blue-300); /* oklch(80.9% 0.105 251.813) */ |
| inset-shadow-blue-400 | --tw-inset-shadow-color: var(--color-blue-400); /* oklch(70.7% 0.165 254.624) */ |
| inset-shadow-blue-500 | --tw-inset-shadow-color: var(--color-blue-500); /* oklch(62.3% 0.214 259.815) */ |
| inset-shadow-blue-600 | --tw-inset-shadow-color: var(--color-blue-600); /* oklch(54.6% 0.245 262.881) */ |
| inset-shadow-blue-700 | --tw-inset-shadow-color: var(--color-blue-700); /* oklch(48.8% 0.243 264.376) */ |
| inset-shadow-blue-800 | --tw-inset-shadow-color: var(--color-blue-800); /* oklch(42.4% 0.199 265.638) */ |
| inset-shadow-blue-900 | --tw-inset-shadow-color: var(--color-blue-900); /* oklch(37.9% 0.146 265.522) */ |
| inset-shadow-blue-950 | --tw-inset-shadow-color: var(--color-blue-950); /* oklch(28.2% 0.091 267.935) */ |
| inset-shadow-indigo-50 | --tw-inset-shadow-color: var(--color-indigo-50); /* oklch(96.2% 0.018 272.314) */ |
| inset-shadow-indigo-100 | --tw-inset-shadow-color: var(--color-indigo-100); /* oklch(93% 0.034 272.788) */ |
| inset-shadow-indigo-200 | --tw-inset-shadow-color: var(--color-indigo-200); /* oklch(87% 0.065 274.039) */ |
| inset-shadow-indigo-300 | --tw-inset-shadow-color: var(--color-indigo-300); /* oklch(78.5% 0.115 274.713) */ |
| inset-shadow-indigo-400 | --tw-inset-shadow-color: var(--color-indigo-400); /* oklch(67.3% 0.182 276.935) */ |
| inset-shadow-indigo-500 | --tw-inset-shadow-color: var(--color-indigo-500); /* oklch(58.5% 0.233 277.117) */ |
| inset-shadow-indigo-600 | --tw-inset-shadow-color: var(--color-indigo-600); /* oklch(51.1% 0.262 276.966) */ |
| inset-shadow-indigo-700 | --tw-inset-shadow-color: var(--color-indigo-700); /* oklch(45.7% 0.24 277.023) */ |
| inset-shadow-indigo-800 | --tw-inset-shadow-color: var(--color-indigo-800); /* oklch(39.8% 0.195 277.366) */ |
| inset-shadow-indigo-900 | --tw-inset-shadow-color: var(--color-indigo-900); /* oklch(35.9% 0.144 278.697) */ |
| inset-shadow-indigo-950 | --tw-inset-shadow-color: var(--color-indigo-950); /* oklch(25.7% 0.09 281.288) */ |
| inset-shadow-violet-50 | --tw-inset-shadow-color: var(--color-violet-50); /* oklch(96.9% 0.016 293.756) */ |
| inset-shadow-violet-100 | --tw-inset-shadow-color: var(--color-violet-100); /* oklch(94.3% 0.029 294.588) */ |
| inset-shadow-violet-200 | --tw-inset-shadow-color: var(--color-violet-200); /* oklch(89.4% 0.057 293.283) */ |
| inset-shadow-violet-300 | --tw-inset-shadow-color: var(--color-violet-300); /* oklch(81.1% 0.111 293.571) */ |
| inset-shadow-violet-400 | --tw-inset-shadow-color: var(--color-violet-400); /* oklch(70.2% 0.183 293.541) */ |
| inset-shadow-violet-500 | --tw-inset-shadow-color: var(--color-violet-500); /* oklch(60.6% 0.25 292.717) */ |
| inset-shadow-violet-600 | --tw-inset-shadow-color: var(--color-violet-600); /* oklch(54.1% 0.281 293.009) */ |
| inset-shadow-violet-700 | --tw-inset-shadow-color: var(--color-violet-700); /* oklch(49.1% 0.27 292.581) */ |
| inset-shadow-violet-800 | --tw-inset-shadow-color: var(--color-violet-800); /* oklch(43.2% 0.232 292.759) */ |
| inset-shadow-violet-900 | --tw-inset-shadow-color: var(--color-violet-900); /* oklch(38% 0.189 293.745) */ |
| inset-shadow-violet-950 | --tw-inset-shadow-color: var(--color-violet-950); /* oklch(28.3% 0.141 291.089) */ |
| inset-shadow-purple-50 | --tw-inset-shadow-color: var(--color-purple-50); /* oklch(97.7% 0.014 308.299) */ |
| inset-shadow-purple-100 | --tw-inset-shadow-color: var(--color-purple-100); /* oklch(94.6% 0.033 307.174) */ |
| inset-shadow-purple-200 | --tw-inset-shadow-color: var(--color-purple-200); /* oklch(90.2% 0.063 306.703) */ |
| inset-shadow-purple-300 | --tw-inset-shadow-color: var(--color-purple-300); /* oklch(82.7% 0.119 306.383) */ |
| inset-shadow-purple-400 | --tw-inset-shadow-color: var(--color-purple-400); /* oklch(71.4% 0.203 305.504) */ |
| inset-shadow-purple-500 | --tw-inset-shadow-color: var(--color-purple-500); /* oklch(62.7% 0.265 303.9) */ |
| inset-shadow-purple-600 | --tw-inset-shadow-color: var(--color-purple-600); /* oklch(55.8% 0.288 302.321) */ |
| inset-shadow-purple-700 | --tw-inset-shadow-color: var(--color-purple-700); /* oklch(49.6% 0.265 301.924) */ |
| inset-shadow-purple-800 | --tw-inset-shadow-color: var(--color-purple-800); /* oklch(43.8% 0.218 303.724) */ |
| inset-shadow-purple-900 | --tw-inset-shadow-color: var(--color-purple-900); /* oklch(38.1% 0.176 304.987) */ |
| inset-shadow-purple-950 | --tw-inset-shadow-color: var(--color-purple-950); /* oklch(29.1% 0.149 302.717) */ |
| inset-shadow-fuchsia-50 | --tw-inset-shadow-color: var(--color-fuchsia-50); /* oklch(97.7% 0.017 320.058) */ |
| inset-shadow-fuchsia-100 | --tw-inset-shadow-color: var(--color-fuchsia-100); /* oklch(95.2% 0.037 318.852) */ |
| inset-shadow-fuchsia-200 | --tw-inset-shadow-color: var(--color-fuchsia-200); /* oklch(90.3% 0.076 319.62) */ |
| inset-shadow-fuchsia-300 | --tw-inset-shadow-color: var(--color-fuchsia-300); /* oklch(83.3% 0.145 321.434) */ |
| inset-shadow-fuchsia-400 | --tw-inset-shadow-color: var(--color-fuchsia-400); /* oklch(74% 0.238 322.16) */ |
| inset-shadow-fuchsia-500 | --tw-inset-shadow-color: var(--color-fuchsia-500); /* oklch(66.7% 0.295 322.15) */ |
| inset-shadow-fuchsia-600 | --tw-inset-shadow-color: var(--color-fuchsia-600); /* oklch(59.1% 0.293 322.896) */ |
| inset-shadow-fuchsia-700 | --tw-inset-shadow-color: var(--color-fuchsia-700); /* oklch(51.8% 0.253 323.949) */ |
| inset-shadow-fuchsia-800 | --tw-inset-shadow-color: var(--color-fuchsia-800); /* oklch(45.2% 0.211 324.591) */ |
| inset-shadow-fuchsia-900 | --tw-inset-shadow-color: var(--color-fuchsia-900); /* oklch(40.1% 0.17 325.612) */ |
| inset-shadow-fuchsia-950 | --tw-inset-shadow-color: var(--color-fuchsia-950); /* oklch(29.3% 0.136 325.661) */ |
| inset-shadow-pink-50 | --tw-inset-shadow-color: var(--color-pink-50); /* oklch(97.1% 0.014 343.198) */ |
| inset-shadow-pink-100 | --tw-inset-shadow-color: var(--color-pink-100); /* oklch(94.8% 0.028 342.258) */ |
| inset-shadow-pink-200 | --tw-inset-shadow-color: var(--color-pink-200); /* oklch(89.9% 0.061 343.231) */ |
| inset-shadow-pink-300 | --tw-inset-shadow-color: var(--color-pink-300); /* oklch(82.3% 0.12 346.018) */ |
| inset-shadow-pink-400 | --tw-inset-shadow-color: var(--color-pink-400); /* oklch(71.8% 0.202 349.761) */ |
| inset-shadow-pink-500 | --tw-inset-shadow-color: var(--color-pink-500); /* oklch(65.6% 0.241 354.308) */ |
| inset-shadow-pink-600 | --tw-inset-shadow-color: var(--color-pink-600); /* oklch(59.2% 0.249 0.584) */ |
| inset-shadow-pink-700 | --tw-inset-shadow-color: var(--color-pink-700); /* oklch(52.5% 0.223 3.958) */ |
| inset-shadow-pink-800 | --tw-inset-shadow-color: var(--color-pink-800); /* oklch(45.9% 0.187 3.815) */ |
| inset-shadow-pink-900 | --tw-inset-shadow-color: var(--color-pink-900); /* oklch(40.8% 0.153 2.432) */ |
| inset-shadow-pink-950 | --tw-inset-shadow-color: var(--color-pink-950); /* oklch(28.4% 0.109 3.907) */ |
| inset-shadow-rose-50 | --tw-inset-shadow-color: var(--color-rose-50); /* oklch(96.9% 0.015 12.422) */ |
| inset-shadow-rose-100 | --tw-inset-shadow-color: var(--color-rose-100); /* oklch(94.1% 0.03 12.58) */ |
| inset-shadow-rose-200 | --tw-inset-shadow-color: var(--color-rose-200); /* oklch(89.2% 0.058 10.001) */ |
| inset-shadow-rose-300 | --tw-inset-shadow-color: var(--color-rose-300); /* oklch(81% 0.117 11.638) */ |
| inset-shadow-rose-400 | --tw-inset-shadow-color: var(--color-rose-400); /* oklch(71.2% 0.194 13.428) */ |
| inset-shadow-rose-500 | --tw-inset-shadow-color: var(--color-rose-500); /* oklch(64.5% 0.246 16.439) */ |
| inset-shadow-rose-600 | --tw-inset-shadow-color: var(--color-rose-600); /* oklch(58.6% 0.253 17.585) */ |
| inset-shadow-rose-700 | --tw-inset-shadow-color: var(--color-rose-700); /* oklch(51.4% 0.222 16.935) */ |
| inset-shadow-rose-800 | --tw-inset-shadow-color: var(--color-rose-800); /* oklch(45.5% 0.188 13.697) */ |
| inset-shadow-rose-900 | --tw-inset-shadow-color: var(--color-rose-900); /* oklch(41% 0.159 10.272) */ |
| inset-shadow-rose-950 | --tw-inset-shadow-color: var(--color-rose-950); /* oklch(27.1% 0.105 12.094) */ |
| inset-shadow-slate-50 | --tw-inset-shadow-color: var(--color-slate-50); /* oklch(98.4% 0.003 247.858) */ |
| inset-shadow-slate-100 | --tw-inset-shadow-color: var(--color-slate-100); /* oklch(96.8% 0.007 247.896) */ |
| inset-shadow-slate-200 | --tw-inset-shadow-color: var(--color-slate-200); /* oklch(92.9% 0.013 255.508) */ |
| inset-shadow-slate-300 | --tw-inset-shadow-color: var(--color-slate-300); /* oklch(86.9% 0.022 252.894) */ |
| inset-shadow-slate-400 | --tw-inset-shadow-color: var(--color-slate-400); /* oklch(70.4% 0.04 256.788) */ |
| inset-shadow-slate-500 | --tw-inset-shadow-color: var(--color-slate-500); /* oklch(55.4% 0.046 257.417) */ |
| inset-shadow-slate-600 | --tw-inset-shadow-color: var(--color-slate-600); /* oklch(44.6% 0.043 257.281) */ |
| inset-shadow-slate-700 | --tw-inset-shadow-color: var(--color-slate-700); /* oklch(37.2% 0.044 257.287) */ |
| inset-shadow-slate-800 | --tw-inset-shadow-color: var(--color-slate-800); /* oklch(27.9% 0.041 260.031) */ |
| inset-shadow-slate-900 | --tw-inset-shadow-color: var(--color-slate-900); /* oklch(20.8% 0.042 265.755) */ |
| inset-shadow-slate-950 | --tw-inset-shadow-color: var(--color-slate-950); /* oklch(12.9% 0.042 264.695) */ |
| inset-shadow-gray-50 | --tw-inset-shadow-color: var(--color-gray-50); /* oklch(98.5% 0.002 247.839) */ |
| inset-shadow-gray-100 | --tw-inset-shadow-color: var(--color-gray-100); /* oklch(96.7% 0.003 264.542) */ |
| inset-shadow-gray-200 | --tw-inset-shadow-color: var(--color-gray-200); /* oklch(92.8% 0.006 264.531) */ |
| inset-shadow-gray-300 | --tw-inset-shadow-color: var(--color-gray-300); /* oklch(87.2% 0.01 258.338) */ |
| inset-shadow-gray-400 | --tw-inset-shadow-color: var(--color-gray-400); /* oklch(70.7% 0.022 261.325) */ |
| inset-shadow-gray-500 | --tw-inset-shadow-color: var(--color-gray-500); /* oklch(55.1% 0.027 264.364) */ |
| inset-shadow-gray-600 | --tw-inset-shadow-color: var(--color-gray-600); /* oklch(44.6% 0.03 256.802) */ |
| inset-shadow-gray-700 | --tw-inset-shadow-color: var(--color-gray-700); /* oklch(37.3% 0.034 259.733) */ |
| inset-shadow-gray-800 | --tw-inset-shadow-color: var(--color-gray-800); /* oklch(27.8% 0.033 256.848) */ |
| inset-shadow-gray-900 | --tw-inset-shadow-color: var(--color-gray-900); /* oklch(21% 0.034 264.665) */ |
| inset-shadow-gray-950 | --tw-inset-shadow-color: var(--color-gray-950); /* oklch(13% 0.028 261.692) */ |
| inset-shadow-zinc-50 | --tw-inset-shadow-color: var(--color-zinc-50); /* oklch(98.5% 0 0) */ |
| inset-shadow-zinc-100 | --tw-inset-shadow-color: var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */ |
| inset-shadow-zinc-200 | --tw-inset-shadow-color: var(--color-zinc-200); /* oklch(92% 0.004 286.32) */ |
| inset-shadow-zinc-300 | --tw-inset-shadow-color: var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */ |
| inset-shadow-zinc-400 | --tw-inset-shadow-color: var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */ |
| inset-shadow-zinc-500 | --tw-inset-shadow-color: var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */ |
| inset-shadow-zinc-600 | --tw-inset-shadow-color: var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */ |
| inset-shadow-zinc-700 | --tw-inset-shadow-color: var(--color-zinc-700); /* oklch(37% 0.013 285.805) */ |
| inset-shadow-zinc-800 | --tw-inset-shadow-color: var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */ |
| inset-shadow-zinc-900 | --tw-inset-shadow-color: var(--color-zinc-900); /* oklch(21% 0.006 285.885) */ |
| inset-shadow-zinc-950 | --tw-inset-shadow-color: var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */ |
| inset-shadow-neutral-50 | --tw-inset-shadow-color: var(--color-neutral-50); /* oklch(98.5% 0 0) */ |
| inset-shadow-neutral-100 | --tw-inset-shadow-color: var(--color-neutral-100); /* oklch(97% 0 0) */ |
| inset-shadow-neutral-200 | --tw-inset-shadow-color: var(--color-neutral-200); /* oklch(92.2% 0 0) */ |
| inset-shadow-neutral-300 | --tw-inset-shadow-color: var(--color-neutral-300); /* oklch(87% 0 0) */ |
| inset-shadow-neutral-400 | --tw-inset-shadow-color: var(--color-neutral-400); /* oklch(70.8% 0 0) */ |
| inset-shadow-neutral-500 | --tw-inset-shadow-color: var(--color-neutral-500); /* oklch(55.6% 0 0) */ |
| inset-shadow-neutral-600 | --tw-inset-shadow-color: var(--color-neutral-600); /* oklch(43.9% 0 0) */ |
| inset-shadow-neutral-700 | --tw-inset-shadow-color: var(--color-neutral-700); /* oklch(37.1% 0 0) */ |
| inset-shadow-neutral-800 | --tw-inset-shadow-color: var(--color-neutral-800); /* oklch(26.9% 0 0) */ |
| inset-shadow-neutral-900 | --tw-inset-shadow-color: var(--color-neutral-900); /* oklch(20.5% 0 0) */ |
| inset-shadow-neutral-950 | --tw-inset-shadow-color: var(--color-neutral-950); /* oklch(14.5% 0 0) */ |
| inset-shadow-stone-50 | --tw-inset-shadow-color: var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */ |
| inset-shadow-stone-100 | --tw-inset-shadow-color: var(--color-stone-100); /* oklch(97% 0.001 106.424) */ |
| inset-shadow-stone-200 | --tw-inset-shadow-color: var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */ |
| inset-shadow-stone-300 | --tw-inset-shadow-color: var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */ |
| inset-shadow-stone-400 | --tw-inset-shadow-color: var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */ |
| inset-shadow-stone-500 | --tw-inset-shadow-color: var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */ |
| inset-shadow-stone-600 | --tw-inset-shadow-color: var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */ |
| inset-shadow-stone-700 | --tw-inset-shadow-color: var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */ |
| inset-shadow-stone-800 | --tw-inset-shadow-color: var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */ |
| inset-shadow-stone-900 | --tw-inset-shadow-color: var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */ |
| inset-shadow-stone-950 | --tw-inset-shadow-color: var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */ |
| ring | --tw-ring-shadow: 0 0 0 1px; |
| ring-<number> | --tw-ring-shadow: 0 0 0 <number>px; |
| ring-(<custom-property>) | --tw-ring-shadow: 0 0 0 var(<custom-property>); |
| ring-[<value>] | --tw-ring-shadow: 0 0 0 <value>; |
| ring-inherit | --tw-ring-color: inherit; |
| ring-current | --tw-ring-color: currentColor; |
| ring-transparent | --tw-ring-color: transparent; |
| ring-black | --tw-ring-color: var(--color-black); /* #000 */ |
| ring-white | --tw-ring-color: var(--color-white); /* #fff */ |
| ring-red-50 | --tw-ring-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */ |
| ring-red-100 | --tw-ring-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */ |
| ring-red-200 | --tw-ring-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */ |
| ring-red-300 | --tw-ring-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */ |
| ring-red-400 | --tw-ring-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */ |
| ring-red-500 | --tw-ring-color: var(--color-red-500); /* oklch(63.7% 0.237 25.331) */ |
| ring-red-600 | --tw-ring-color: var(--color-red-600); /* oklch(57.7% 0.245 27.325) */ |
| ring-red-700 | --tw-ring-color: var(--color-red-700); /* oklch(50.5% 0.213 27.518) */ |
| ring-red-800 | --tw-ring-color: var(--color-red-800); /* oklch(44.4% 0.177 26.899) */ |
| ring-red-900 | --tw-ring-color: var(--color-red-900); /* oklch(39.6% 0.141 25.723) */ |
| ring-red-950 | --tw-ring-color: var(--color-red-950); /* oklch(25.8% 0.092 26.042) */ |
| ring-orange-50 | --tw-ring-color: var(--color-orange-50); /* oklch(98% 0.016 73.684) */ |
| ring-orange-100 | --tw-ring-color: var(--color-orange-100); /* oklch(95.4% 0.038 75.164) */ |
| ring-orange-200 | --tw-ring-color: var(--color-orange-200); /* oklch(90.1% 0.076 70.697) */ |
| ring-orange-300 | --tw-ring-color: var(--color-orange-300); /* oklch(83.7% 0.128 66.29) */ |
| ring-orange-400 | --tw-ring-color: var(--color-orange-400); /* oklch(75% 0.183 55.934) */ |
| ring-orange-500 | --tw-ring-color: var(--color-orange-500); /* oklch(70.5% 0.213 47.604) */ |
| ring-orange-600 | --tw-ring-color: var(--color-orange-600); /* oklch(64.6% 0.222 41.116) */ |
| ring-orange-700 | --tw-ring-color: var(--color-orange-700); /* oklch(55.3% 0.195 38.402) */ |
| ring-orange-800 | --tw-ring-color: var(--color-orange-800); /* oklch(47% 0.157 37.304) */ |
| ring-orange-900 | --tw-ring-color: var(--color-orange-900); /* oklch(40.8% 0.123 38.172) */ |
| ring-orange-950 | --tw-ring-color: var(--color-orange-950); /* oklch(26.6% 0.079 36.259) */ |
| ring-amber-50 | --tw-ring-color: var(--color-amber-50); /* oklch(98.7% 0.022 95.277) */ |
| ring-amber-100 | --tw-ring-color: var(--color-amber-100); /* oklch(96.2% 0.059 95.617) */ |
| ring-amber-200 | --tw-ring-color: var(--color-amber-200); /* oklch(92.4% 0.12 95.746) */ |
| ring-amber-300 | --tw-ring-color: var(--color-amber-300); /* oklch(87.9% 0.169 91.605) */ |
| ring-amber-400 | --tw-ring-color: var(--color-amber-400); /* oklch(82.8% 0.189 84.429) */ |
| ring-amber-500 | --tw-ring-color: var(--color-amber-500); /* oklch(76.9% 0.188 70.08) */ |
| ring-amber-600 | --tw-ring-color: var(--color-amber-600); /* oklch(66.6% 0.179 58.318) */ |
| ring-amber-700 | --tw-ring-color: var(--color-amber-700); /* oklch(55.5% 0.163 48.998) */ |
| ring-amber-800 | --tw-ring-color: var(--color-amber-800); /* oklch(47.3% 0.137 46.201) */ |
| ring-amber-900 | --tw-ring-color: var(--color-amber-900); /* oklch(41.4% 0.112 45.904) */ |
| ring-amber-950 | --tw-ring-color: var(--color-amber-950); /* oklch(27.9% 0.077 45.635) */ |
| ring-yellow-50 | --tw-ring-color: var(--color-yellow-50); /* oklch(98.7% 0.026 102.212) */ |
| ring-yellow-100 | --tw-ring-color: var(--color-yellow-100); /* oklch(97.3% 0.071 103.193) */ |
| ring-yellow-200 | --tw-ring-color: var(--color-yellow-200); /* oklch(94.5% 0.129 101.54) */ |
| ring-yellow-300 | --tw-ring-color: var(--color-yellow-300); /* oklch(90.5% 0.182 98.111) */ |
| ring-yellow-400 | --tw-ring-color: var(--color-yellow-400); /* oklch(85.2% 0.199 91.936) */ |
| ring-yellow-500 | --tw-ring-color: var(--color-yellow-500); /* oklch(79.5% 0.184 86.047) */ |
| ring-yellow-600 | --tw-ring-color: var(--color-yellow-600); /* oklch(68.1% 0.162 75.834) */ |
| ring-yellow-700 | --tw-ring-color: var(--color-yellow-700); /* oklch(55.4% 0.135 66.442) */ |
| ring-yellow-800 | --tw-ring-color: var(--color-yellow-800); /* oklch(47.6% 0.114 61.907) */ |
| ring-yellow-900 | --tw-ring-color: var(--color-yellow-900); /* oklch(42.1% 0.095 57.708) */ |
| ring-yellow-950 | --tw-ring-color: var(--color-yellow-950); /* oklch(28.6% 0.066 53.813) */ |
| ring-lime-50 | --tw-ring-color: var(--color-lime-50); /* oklch(98.6% 0.031 120.757) */ |
| ring-lime-100 | --tw-ring-color: var(--color-lime-100); /* oklch(96.7% 0.067 122.328) */ |
| ring-lime-200 | --tw-ring-color: var(--color-lime-200); /* oklch(93.8% 0.127 124.321) */ |
| ring-lime-300 | --tw-ring-color: var(--color-lime-300); /* oklch(89.7% 0.196 126.665) */ |
| ring-lime-400 | --tw-ring-color: var(--color-lime-400); /* oklch(84.1% 0.238 128.85) */ |
| ring-lime-500 | --tw-ring-color: var(--color-lime-500); /* oklch(76.8% 0.233 130.85) */ |
| ring-lime-600 | --tw-ring-color: var(--color-lime-600); /* oklch(64.8% 0.2 131.684) */ |
| ring-lime-700 | --tw-ring-color: var(--color-lime-700); /* oklch(53.2% 0.157 131.589) */ |
| ring-lime-800 | --tw-ring-color: var(--color-lime-800); /* oklch(45.3% 0.124 130.933) */ |
| ring-lime-900 | --tw-ring-color: var(--color-lime-900); /* oklch(40.5% 0.101 131.063) */ |
| ring-lime-950 | --tw-ring-color: var(--color-lime-950); /* oklch(27.4% 0.072 132.109) */ |
| ring-green-50 | --tw-ring-color: var(--color-green-50); /* oklch(98.2% 0.018 155.826) */ |
| ring-green-100 | --tw-ring-color: var(--color-green-100); /* oklch(96.2% 0.044 156.743) */ |
| ring-green-200 | --tw-ring-color: var(--color-green-200); /* oklch(92.5% 0.084 155.995) */ |
| ring-green-300 | --tw-ring-color: var(--color-green-300); /* oklch(87.1% 0.15 154.449) */ |
| ring-green-400 | --tw-ring-color: var(--color-green-400); /* oklch(79.2% 0.209 151.711) */ |
| ring-green-500 | --tw-ring-color: var(--color-green-500); /* oklch(72.3% 0.219 149.579) */ |
| ring-green-600 | --tw-ring-color: var(--color-green-600); /* oklch(62.7% 0.194 149.214) */ |
| ring-green-700 | --tw-ring-color: var(--color-green-700); /* oklch(52.7% 0.154 150.069) */ |
| ring-green-800 | --tw-ring-color: var(--color-green-800); /* oklch(44.8% 0.119 151.328) */ |
| ring-green-900 | --tw-ring-color: var(--color-green-900); /* oklch(39.3% 0.095 152.535) */ |
| ring-green-950 | --tw-ring-color: var(--color-green-950); /* oklch(26.6% 0.065 152.934) */ |
| ring-emerald-50 | --tw-ring-color: var(--color-emerald-50); /* oklch(97.9% 0.021 166.113) */ |
| ring-emerald-100 | --tw-ring-color: var(--color-emerald-100); /* oklch(95% 0.052 163.051) */ |
| ring-emerald-200 | --tw-ring-color: var(--color-emerald-200); /* oklch(90.5% 0.093 164.15) */ |
| ring-emerald-300 | --tw-ring-color: var(--color-emerald-300); /* oklch(84.5% 0.143 164.978) */ |
| ring-emerald-400 | --tw-ring-color: var(--color-emerald-400); /* oklch(76.5% 0.177 163.223) */ |
| ring-emerald-500 | --tw-ring-color: var(--color-emerald-500); /* oklch(69.6% 0.17 162.48) */ |
| ring-emerald-600 | --tw-ring-color: var(--color-emerald-600); /* oklch(59.6% 0.145 163.225) */ |
| ring-emerald-700 | --tw-ring-color: var(--color-emerald-700); /* oklch(50.8% 0.118 165.612) */ |
| ring-emerald-800 | --tw-ring-color: var(--color-emerald-800); /* oklch(43.2% 0.095 166.913) */ |
| ring-emerald-900 | --tw-ring-color: var(--color-emerald-900); /* oklch(37.8% 0.077 168.94) */ |
| ring-emerald-950 | --tw-ring-color: var(--color-emerald-950); /* oklch(26.2% 0.051 172.552) */ |
| ring-teal-50 | --tw-ring-color: var(--color-teal-50); /* oklch(98.4% 0.014 180.72) */ |
| ring-teal-100 | --tw-ring-color: var(--color-teal-100); /* oklch(95.3% 0.051 180.801) */ |
| ring-teal-200 | --tw-ring-color: var(--color-teal-200); /* oklch(91% 0.096 180.426) */ |
| ring-teal-300 | --tw-ring-color: var(--color-teal-300); /* oklch(85.5% 0.138 181.071) */ |
| ring-teal-400 | --tw-ring-color: var(--color-teal-400); /* oklch(77.7% 0.152 181.912) */ |
| ring-teal-500 | --tw-ring-color: var(--color-teal-500); /* oklch(70.4% 0.14 182.503) */ |
| ring-teal-600 | --tw-ring-color: var(--color-teal-600); /* oklch(60% 0.118 184.704) */ |
| ring-teal-700 | --tw-ring-color: var(--color-teal-700); /* oklch(51.1% 0.096 186.391) */ |
| ring-teal-800 | --tw-ring-color: var(--color-teal-800); /* oklch(43.7% 0.078 188.216) */ |
| ring-teal-900 | --tw-ring-color: var(--color-teal-900); /* oklch(38.6% 0.063 188.416) */ |
| ring-teal-950 | --tw-ring-color: var(--color-teal-950); /* oklch(27.7% 0.046 192.524) */ |
| ring-cyan-50 | --tw-ring-color: var(--color-cyan-50); /* oklch(98.4% 0.019 200.873) */ |
| ring-cyan-100 | --tw-ring-color: var(--color-cyan-100); /* oklch(95.6% 0.045 203.388) */ |
| ring-cyan-200 | --tw-ring-color: var(--color-cyan-200); /* oklch(91.7% 0.08 205.041) */ |
| ring-cyan-300 | --tw-ring-color: var(--color-cyan-300); /* oklch(86.5% 0.127 207.078) */ |
| ring-cyan-400 | --tw-ring-color: var(--color-cyan-400); /* oklch(78.9% 0.154 211.53) */ |
| ring-cyan-500 | --tw-ring-color: var(--color-cyan-500); /* oklch(71.5% 0.143 215.221) */ |
| ring-cyan-600 | --tw-ring-color: var(--color-cyan-600); /* oklch(60.9% 0.126 221.723) */ |
| ring-cyan-700 | --tw-ring-color: var(--color-cyan-700); /* oklch(52% 0.105 223.128) */ |
| ring-cyan-800 | --tw-ring-color: var(--color-cyan-800); /* oklch(45% 0.085 224.283) */ |
| ring-cyan-900 | --tw-ring-color: var(--color-cyan-900); /* oklch(39.8% 0.07 227.392) */ |
| ring-cyan-950 | --tw-ring-color: var(--color-cyan-950); /* oklch(30.2% 0.056 229.695) */ |
| ring-sky-50 | --tw-ring-color: var(--color-sky-50); /* oklch(97.7% 0.013 236.62) */ |
| ring-sky-100 | --tw-ring-color: var(--color-sky-100); /* oklch(95.1% 0.026 236.824) */ |
| ring-sky-200 | --tw-ring-color: var(--color-sky-200); /* oklch(90.1% 0.058 230.902) */ |
| ring-sky-300 | --tw-ring-color: var(--color-sky-300); /* oklch(82.8% 0.111 230.318) */ |
| ring-sky-400 | --tw-ring-color: var(--color-sky-400); /* oklch(74.6% 0.16 232.661) */ |
| ring-sky-500 | --tw-ring-color: var(--color-sky-500); /* oklch(68.5% 0.169 237.323) */ |
| ring-sky-600 | --tw-ring-color: var(--color-sky-600); /* oklch(58.8% 0.158 241.966) */ |
| ring-sky-700 | --tw-ring-color: var(--color-sky-700); /* oklch(50% 0.134 242.749) */ |
| ring-sky-800 | --tw-ring-color: var(--color-sky-800); /* oklch(44.3% 0.11 240.79) */ |
| ring-sky-900 | --tw-ring-color: var(--color-sky-900); /* oklch(39.1% 0.09 240.876) */ |
| ring-sky-950 | --tw-ring-color: var(--color-sky-950); /* oklch(29.3% 0.066 243.157) */ |
| ring-blue-50 | --tw-ring-color: var(--color-blue-50); /* oklch(97% 0.014 254.604) */ |
| ring-blue-100 | --tw-ring-color: var(--color-blue-100); /* oklch(93.2% 0.032 255.585) */ |
| ring-blue-200 | --tw-ring-color: var(--color-blue-200); /* oklch(88.2% 0.059 254.128) */ |
| ring-blue-300 | --tw-ring-color: var(--color-blue-300); /* oklch(80.9% 0.105 251.813) */ |
| ring-blue-400 | --tw-ring-color: var(--color-blue-400); /* oklch(70.7% 0.165 254.624) */ |
| ring-blue-500 | --tw-ring-color: var(--color-blue-500); /* oklch(62.3% 0.214 259.815) */ |
| ring-blue-600 | --tw-ring-color: var(--color-blue-600); /* oklch(54.6% 0.245 262.881) */ |
| ring-blue-700 | --tw-ring-color: var(--color-blue-700); /* oklch(48.8% 0.243 264.376) */ |
| ring-blue-800 | --tw-ring-color: var(--color-blue-800); /* oklch(42.4% 0.199 265.638) */ |
| ring-blue-900 | --tw-ring-color: var(--color-blue-900); /* oklch(37.9% 0.146 265.522) */ |
| ring-blue-950 | --tw-ring-color: var(--color-blue-950); /* oklch(28.2% 0.091 267.935) */ |
| ring-indigo-50 | --tw-ring-color: var(--color-indigo-50); /* oklch(96.2% 0.018 272.314) */ |
| ring-indigo-100 | --tw-ring-color: var(--color-indigo-100); /* oklch(93% 0.034 272.788) */ |
| ring-indigo-200 | --tw-ring-color: var(--color-indigo-200); /* oklch(87% 0.065 274.039) */ |
| ring-indigo-300 | --tw-ring-color: var(--color-indigo-300); /* oklch(78.5% 0.115 274.713) */ |
| ring-indigo-400 | --tw-ring-color: var(--color-indigo-400); /* oklch(67.3% 0.182 276.935) */ |
| ring-indigo-500 | --tw-ring-color: var(--color-indigo-500); /* oklch(58.5% 0.233 277.117) */ |
| ring-indigo-600 | --tw-ring-color: var(--color-indigo-600); /* oklch(51.1% 0.262 276.966) */ |
| ring-indigo-700 | --tw-ring-color: var(--color-indigo-700); /* oklch(45.7% 0.24 277.023) */ |
| ring-indigo-800 | --tw-ring-color: var(--color-indigo-800); /* oklch(39.8% 0.195 277.366) */ |
| ring-indigo-900 | --tw-ring-color: var(--color-indigo-900); /* oklch(35.9% 0.144 278.697) */ |
| ring-indigo-950 | --tw-ring-color: var(--color-indigo-950); /* oklch(25.7% 0.09 281.288) */ |
| ring-violet-50 | --tw-ring-color: var(--color-violet-50); /* oklch(96.9% 0.016 293.756) */ |
| ring-violet-100 | --tw-ring-color: var(--color-violet-100); /* oklch(94.3% 0.029 294.588) */ |
| ring-violet-200 | --tw-ring-color: var(--color-violet-200); /* oklch(89.4% 0.057 293.283) */ |
| ring-violet-300 | --tw-ring-color: var(--color-violet-300); /* oklch(81.1% 0.111 293.571) */ |
| ring-violet-400 | --tw-ring-color: var(--color-violet-400); /* oklch(70.2% 0.183 293.541) */ |
| ring-violet-500 | --tw-ring-color: var(--color-violet-500); /* oklch(60.6% 0.25 292.717) */ |
| ring-violet-600 | --tw-ring-color: var(--color-violet-600); /* oklch(54.1% 0.281 293.009) */ |
| ring-violet-700 | --tw-ring-color: var(--color-violet-700); /* oklch(49.1% 0.27 292.581) */ |
| ring-violet-800 | --tw-ring-color: var(--color-violet-800); /* oklch(43.2% 0.232 292.759) */ |
| ring-violet-900 | --tw-ring-color: var(--color-violet-900); /* oklch(38% 0.189 293.745) */ |
| ring-violet-950 | --tw-ring-color: var(--color-violet-950); /* oklch(28.3% 0.141 291.089) */ |
| ring-purple-50 | --tw-ring-color: var(--color-purple-50); /* oklch(97.7% 0.014 308.299) */ |
| ring-purple-100 | --tw-ring-color: var(--color-purple-100); /* oklch(94.6% 0.033 307.174) */ |
| ring-purple-200 | --tw-ring-color: var(--color-purple-200); /* oklch(90.2% 0.063 306.703) */ |
| ring-purple-300 | --tw-ring-color: var(--color-purple-300); /* oklch(82.7% 0.119 306.383) */ |
| ring-purple-400 | --tw-ring-color: var(--color-purple-400); /* oklch(71.4% 0.203 305.504) */ |
| ring-purple-500 | --tw-ring-color: var(--color-purple-500); /* oklch(62.7% 0.265 303.9) */ |
| ring-purple-600 | --tw-ring-color: var(--color-purple-600); /* oklch(55.8% 0.288 302.321) */ |
| ring-purple-700 | --tw-ring-color: var(--color-purple-700); /* oklch(49.6% 0.265 301.924) */ |
| ring-purple-800 | --tw-ring-color: var(--color-purple-800); /* oklch(43.8% 0.218 303.724) */ |
| ring-purple-900 | --tw-ring-color: var(--color-purple-900); /* oklch(38.1% 0.176 304.987) */ |
| ring-purple-950 | --tw-ring-color: var(--color-purple-950); /* oklch(29.1% 0.149 302.717) */ |
| ring-fuchsia-50 | --tw-ring-color: var(--color-fuchsia-50); /* oklch(97.7% 0.017 320.058) */ |
| ring-fuchsia-100 | --tw-ring-color: var(--color-fuchsia-100); /* oklch(95.2% 0.037 318.852) */ |
| ring-fuchsia-200 | --tw-ring-color: var(--color-fuchsia-200); /* oklch(90.3% 0.076 319.62) */ |
| ring-fuchsia-300 | --tw-ring-color: var(--color-fuchsia-300); /* oklch(83.3% 0.145 321.434) */ |
| ring-fuchsia-400 | --tw-ring-color: var(--color-fuchsia-400); /* oklch(74% 0.238 322.16) */ |
| ring-fuchsia-500 | --tw-ring-color: var(--color-fuchsia-500); /* oklch(66.7% 0.295 322.15) */ |
| ring-fuchsia-600 | --tw-ring-color: var(--color-fuchsia-600); /* oklch(59.1% 0.293 322.896) */ |
| ring-fuchsia-700 | --tw-ring-color: var(--color-fuchsia-700); /* oklch(51.8% 0.253 323.949) */ |
| ring-fuchsia-800 | --tw-ring-color: var(--color-fuchsia-800); /* oklch(45.2% 0.211 324.591) */ |
| ring-fuchsia-900 | --tw-ring-color: var(--color-fuchsia-900); /* oklch(40.1% 0.17 325.612) */ |
| ring-fuchsia-950 | --tw-ring-color: var(--color-fuchsia-950); /* oklch(29.3% 0.136 325.661) */ |
| ring-pink-50 | --tw-ring-color: var(--color-pink-50); /* oklch(97.1% 0.014 343.198) */ |
| ring-pink-100 | --tw-ring-color: var(--color-pink-100); /* oklch(94.8% 0.028 342.258) */ |
| ring-pink-200 | --tw-ring-color: var(--color-pink-200); /* oklch(89.9% 0.061 343.231) */ |
| ring-pink-300 | --tw-ring-color: var(--color-pink-300); /* oklch(82.3% 0.12 346.018) */ |
| ring-pink-400 | --tw-ring-color: var(--color-pink-400); /* oklch(71.8% 0.202 349.761) */ |
| ring-pink-500 | --tw-ring-color: var(--color-pink-500); /* oklch(65.6% 0.241 354.308) */ |
| ring-pink-600 | --tw-ring-color: var(--color-pink-600); /* oklch(59.2% 0.249 0.584) */ |
| ring-pink-700 | --tw-ring-color: var(--color-pink-700); /* oklch(52.5% 0.223 3.958) */ |
| ring-pink-800 | --tw-ring-color: var(--color-pink-800); /* oklch(45.9% 0.187 3.815) */ |
| ring-pink-900 | --tw-ring-color: var(--color-pink-900); /* oklch(40.8% 0.153 2.432) */ |
| ring-pink-950 | --tw-ring-color: var(--color-pink-950); /* oklch(28.4% 0.109 3.907) */ |
| ring-rose-50 | --tw-ring-color: var(--color-rose-50); /* oklch(96.9% 0.015 12.422) */ |
| ring-rose-100 | --tw-ring-color: var(--color-rose-100); /* oklch(94.1% 0.03 12.58) */ |
| ring-rose-200 | --tw-ring-color: var(--color-rose-200); /* oklch(89.2% 0.058 10.001) */ |
| ring-rose-300 | --tw-ring-color: var(--color-rose-300); /* oklch(81% 0.117 11.638) */ |
| ring-rose-400 | --tw-ring-color: var(--color-rose-400); /* oklch(71.2% 0.194 13.428) */ |
| ring-rose-500 | --tw-ring-color: var(--color-rose-500); /* oklch(64.5% 0.246 16.439) */ |
| ring-rose-600 | --tw-ring-color: var(--color-rose-600); /* oklch(58.6% 0.253 17.585) */ |
| ring-rose-700 | --tw-ring-color: var(--color-rose-700); /* oklch(51.4% 0.222 16.935) */ |
| ring-rose-800 | --tw-ring-color: var(--color-rose-800); /* oklch(45.5% 0.188 13.697) */ |
| ring-rose-900 | --tw-ring-color: var(--color-rose-900); /* oklch(41% 0.159 10.272) */ |
| ring-rose-950 | --tw-ring-color: var(--color-rose-950); /* oklch(27.1% 0.105 12.094) */ |
| ring-slate-50 | --tw-ring-color: var(--color-slate-50); /* oklch(98.4% 0.003 247.858) */ |
| ring-slate-100 | --tw-ring-color: var(--color-slate-100); /* oklch(96.8% 0.007 247.896) */ |
| ring-slate-200 | --tw-ring-color: var(--color-slate-200); /* oklch(92.9% 0.013 255.508) */ |
| ring-slate-300 | --tw-ring-color: var(--color-slate-300); /* oklch(86.9% 0.022 252.894) */ |
| ring-slate-400 | --tw-ring-color: var(--color-slate-400); /* oklch(70.4% 0.04 256.788) */ |
| ring-slate-500 | --tw-ring-color: var(--color-slate-500); /* oklch(55.4% 0.046 257.417) */ |
| ring-slate-600 | --tw-ring-color: var(--color-slate-600); /* oklch(44.6% 0.043 257.281) */ |
| ring-slate-700 | --tw-ring-color: var(--color-slate-700); /* oklch(37.2% 0.044 257.287) */ |
| ring-slate-800 | --tw-ring-color: var(--color-slate-800); /* oklch(27.9% 0.041 260.031) */ |
| ring-slate-900 | --tw-ring-color: var(--color-slate-900); /* oklch(20.8% 0.042 265.755) */ |
| ring-slate-950 | --tw-ring-color: var(--color-slate-950); /* oklch(12.9% 0.042 264.695) */ |
| ring-gray-50 | --tw-ring-color: var(--color-gray-50); /* oklch(98.5% 0.002 247.839) */ |
| ring-gray-100 | --tw-ring-color: var(--color-gray-100); /* oklch(96.7% 0.003 264.542) */ |
| ring-gray-200 | --tw-ring-color: var(--color-gray-200); /* oklch(92.8% 0.006 264.531) */ |
| ring-gray-300 | --tw-ring-color: var(--color-gray-300); /* oklch(87.2% 0.01 258.338) */ |
| ring-gray-400 | --tw-ring-color: var(--color-gray-400); /* oklch(70.7% 0.022 261.325) */ |
| ring-gray-500 | --tw-ring-color: var(--color-gray-500); /* oklch(55.1% 0.027 264.364) */ |
| ring-gray-600 | --tw-ring-color: var(--color-gray-600); /* oklch(44.6% 0.03 256.802) */ |
| ring-gray-700 | --tw-ring-color: var(--color-gray-700); /* oklch(37.3% 0.034 259.733) */ |
| ring-gray-800 | --tw-ring-color: var(--color-gray-800); /* oklch(27.8% 0.033 256.848) */ |
| ring-gray-900 | --tw-ring-color: var(--color-gray-900); /* oklch(21% 0.034 264.665) */ |
| ring-gray-950 | --tw-ring-color: var(--color-gray-950); /* oklch(13% 0.028 261.692) */ |
| ring-zinc-50 | --tw-ring-color: var(--color-zinc-50); /* oklch(98.5% 0 0) */ |
| ring-zinc-100 | --tw-ring-color: var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */ |
| ring-zinc-200 | --tw-ring-color: var(--color-zinc-200); /* oklch(92% 0.004 286.32) */ |
| ring-zinc-300 | --tw-ring-color: var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */ |
| ring-zinc-400 | --tw-ring-color: var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */ |
| ring-zinc-500 | --tw-ring-color: var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */ |
| ring-zinc-600 | --tw-ring-color: var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */ |
| ring-zinc-700 | --tw-ring-color: var(--color-zinc-700); /* oklch(37% 0.013 285.805) */ |
| ring-zinc-800 | --tw-ring-color: var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */ |
| ring-zinc-900 | --tw-ring-color: var(--color-zinc-900); /* oklch(21% 0.006 285.885) */ |
| ring-zinc-950 | --tw-ring-color: var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */ |
| ring-neutral-50 | --tw-ring-color: var(--color-neutral-50); /* oklch(98.5% 0 0) */ |
| ring-neutral-100 | --tw-ring-color: var(--color-neutral-100); /* oklch(97% 0 0) */ |
| ring-neutral-200 | --tw-ring-color: var(--color-neutral-200); /* oklch(92.2% 0 0) */ |
| ring-neutral-300 | --tw-ring-color: var(--color-neutral-300); /* oklch(87% 0 0) */ |
| ring-neutral-400 | --tw-ring-color: var(--color-neutral-400); /* oklch(70.8% 0 0) */ |
| ring-neutral-500 | --tw-ring-color: var(--color-neutral-500); /* oklch(55.6% 0 0) */ |
| ring-neutral-600 | --tw-ring-color: var(--color-neutral-600); /* oklch(43.9% 0 0) */ |
| ring-neutral-700 | --tw-ring-color: var(--color-neutral-700); /* oklch(37.1% 0 0) */ |
| ring-neutral-800 | --tw-ring-color: var(--color-neutral-800); /* oklch(26.9% 0 0) */ |
| ring-neutral-900 | --tw-ring-color: var(--color-neutral-900); /* oklch(20.5% 0 0) */ |
| ring-neutral-950 | --tw-ring-color: var(--color-neutral-950); /* oklch(14.5% 0 0) */ |
| ring-stone-50 | --tw-ring-color: var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */ |
| ring-stone-100 | --tw-ring-color: var(--color-stone-100); /* oklch(97% 0.001 106.424) */ |
| ring-stone-200 | --tw-ring-color: var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */ |
| ring-stone-300 | --tw-ring-color: var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */ |
| ring-stone-400 | --tw-ring-color: var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */ |
| ring-stone-500 | --tw-ring-color: var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */ |
| ring-stone-600 | --tw-ring-color: var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */ |
| ring-stone-700 | --tw-ring-color: var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */ |
| ring-stone-800 | --tw-ring-color: var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */ |
| ring-stone-900 | --tw-ring-color: var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */ |
| ring-stone-950 | --tw-ring-color: var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */ |
| inset-ring | --tw-inset-ring-shadow: inset 0 0 0 1px |
| inset-ring-<number> | --tw-inset-ring-shadow: inset 0 0 0 <number>px |
| inset-ring-(<custom-property>) | --tw-inset-ring-shadow: inset 0 0 0 var(<custom-property>); |
| inset-ring-[<value>] | --tw-inset-ring-shadow: inset 0 0 0 <value>; |
| inset-ring-inherit | --tw-inset-ring-color: inherit; |
| inset-ring-current | --tw-inset-ring-color: currentColor; |
| inset-ring-transparent | --tw-inset-ring-color: transparent; |
| inset-ring-black | --tw-inset-ring-color: var(--color-black); /* #000 */ |
| inset-ring-white | --tw-inset-ring-color: var(--color-white); /* #fff */ |
| inset-ring-red-50 | --tw-inset-ring-color: var(--color-red-50); /* oklch(97.1% 0.013 17.38) */ |
| inset-ring-red-100 | --tw-inset-ring-color: var(--color-red-100); /* oklch(93.6% 0.032 17.717) */ |
| inset-ring-red-200 | --tw-inset-ring-color: var(--color-red-200); /* oklch(88.5% 0.062 18.334) */ |
| inset-ring-red-300 | --tw-inset-ring-color: var(--color-red-300); /* oklch(80.8% 0.114 19.571) */ |
| inset-ring-red-400 | --tw-inset-ring-color: var(--color-red-400); /* oklch(70.4% 0.191 22.216) */ |
| inset-ring-red-500 | --tw-inset-ring-color: var(--color-red-500); /* oklch(63.7% 0.237 25.331) */ |
| inset-ring-red-600 | --tw-inset-ring-color: var(--color-red-600); /* oklch(57.7% 0.245 27.325) */ |
| inset-ring-red-700 | --tw-inset-ring-color: var(--color-red-700); /* oklch(50.5% 0.213 27.518) */ |
| inset-ring-red-800 | --tw-inset-ring-color: var(--color-red-800); /* oklch(44.4% 0.177 26.899) */ |
| inset-ring-red-900 | --tw-inset-ring-color: var(--color-red-900); /* oklch(39.6% 0.141 25.723) */ |
| inset-ring-red-950 | --tw-inset-ring-color: var(--color-red-950); /* oklch(25.8% 0.092 26.042) */ |
| inset-ring-orange-50 | --tw-inset-ring-color: var(--color-orange-50); /* oklch(98% 0.016 73.684) */ |
| inset-ring-orange-100 | --tw-inset-ring-color: var(--color-orange-100); /* oklch(95.4% 0.038 75.164) */ |
| inset-ring-orange-200 | --tw-inset-ring-color: var(--color-orange-200); /* oklch(90.1% 0.076 70.697) */ |
| inset-ring-orange-300 | --tw-inset-ring-color: var(--color-orange-300); /* oklch(83.7% 0.128 66.29) */ |
| inset-ring-orange-400 | --tw-inset-ring-color: var(--color-orange-400); /* oklch(75% 0.183 55.934) */ |
| inset-ring-orange-500 | --tw-inset-ring-color: var(--color-orange-500); /* oklch(70.5% 0.213 47.604) */ |
| inset-ring-orange-600 | --tw-inset-ring-color: var(--color-orange-600); /* oklch(64.6% 0.222 41.116) */ |
| inset-ring-orange-700 | --tw-inset-ring-color: var(--color-orange-700); /* oklch(55.3% 0.195 38.402) */ |
| inset-ring-orange-800 | --tw-inset-ring-color: var(--color-orange-800); /* oklch(47% 0.157 37.304) */ |
| inset-ring-orange-900 | --tw-inset-ring-color: var(--color-orange-900); /* oklch(40.8% 0.123 38.172) */ |
| inset-ring-orange-950 | --tw-inset-ring-color: var(--color-orange-950); /* oklch(26.6% 0.079 36.259) */ |
| inset-ring-amber-50 | --tw-inset-ring-color: var(--color-amber-50); /* oklch(98.7% 0.022 95.277) */ |
| inset-ring-amber-100 | --tw-inset-ring-color: var(--color-amber-100); /* oklch(96.2% 0.059 95.617) */ |
| inset-ring-amber-200 | --tw-inset-ring-color: var(--color-amber-200); /* oklch(92.4% 0.12 95.746) */ |
| inset-ring-amber-300 | --tw-inset-ring-color: var(--color-amber-300); /* oklch(87.9% 0.169 91.605) */ |
| inset-ring-amber-400 | --tw-inset-ring-color: var(--color-amber-400); /* oklch(82.8% 0.189 84.429) */ |
| inset-ring-amber-500 | --tw-inset-ring-color: var(--color-amber-500); /* oklch(76.9% 0.188 70.08) */ |
| inset-ring-amber-600 | --tw-inset-ring-color: var(--color-amber-600); /* oklch(66.6% 0.179 58.318) */ |
| inset-ring-amber-700 | --tw-inset-ring-color: var(--color-amber-700); /* oklch(55.5% 0.163 48.998) */ |
| inset-ring-amber-800 | --tw-inset-ring-color: var(--color-amber-800); /* oklch(47.3% 0.137 46.201) */ |
| inset-ring-amber-900 | --tw-inset-ring-color: var(--color-amber-900); /* oklch(41.4% 0.112 45.904) */ |
| inset-ring-amber-950 | --tw-inset-ring-color: var(--color-amber-950); /* oklch(27.9% 0.077 45.635) */ |
| inset-ring-yellow-50 | --tw-inset-ring-color: var(--color-yellow-50); /* oklch(98.7% 0.026 102.212) */ |
| inset-ring-yellow-100 | --tw-inset-ring-color: var(--color-yellow-100); /* oklch(97.3% 0.071 103.193) */ |
| inset-ring-yellow-200 | --tw-inset-ring-color: var(--color-yellow-200); /* oklch(94.5% 0.129 101.54) */ |
| inset-ring-yellow-300 | --tw-inset-ring-color: var(--color-yellow-300); /* oklch(90.5% 0.182 98.111) */ |
| inset-ring-yellow-400 | --tw-inset-ring-color: var(--color-yellow-400); /* oklch(85.2% 0.199 91.936) */ |
| inset-ring-yellow-500 | --tw-inset-ring-color: var(--color-yellow-500); /* oklch(79.5% 0.184 86.047) */ |
| inset-ring-yellow-600 | --tw-inset-ring-color: var(--color-yellow-600); /* oklch(68.1% 0.162 75.834) */ |
| inset-ring-yellow-700 | --tw-inset-ring-color: var(--color-yellow-700); /* oklch(55.4% 0.135 66.442) */ |
| inset-ring-yellow-800 | --tw-inset-ring-color: var(--color-yellow-800); /* oklch(47.6% 0.114 61.907) */ |
| inset-ring-yellow-900 | --tw-inset-ring-color: var(--color-yellow-900); /* oklch(42.1% 0.095 57.708) */ |
| inset-ring-yellow-950 | --tw-inset-ring-color: var(--color-yellow-950); /* oklch(28.6% 0.066 53.813) */ |
| inset-ring-lime-50 | --tw-inset-ring-color: var(--color-lime-50); /* oklch(98.6% 0.031 120.757) */ |
| inset-ring-lime-100 | --tw-inset-ring-color: var(--color-lime-100); /* oklch(96.7% 0.067 122.328) */ |
| inset-ring-lime-200 | --tw-inset-ring-color: var(--color-lime-200); /* oklch(93.8% 0.127 124.321) */ |
| inset-ring-lime-300 | --tw-inset-ring-color: var(--color-lime-300); /* oklch(89.7% 0.196 126.665) */ |
| inset-ring-lime-400 | --tw-inset-ring-color: var(--color-lime-400); /* oklch(84.1% 0.238 128.85) */ |
| inset-ring-lime-500 | --tw-inset-ring-color: var(--color-lime-500); /* oklch(76.8% 0.233 130.85) */ |
| inset-ring-lime-600 | --tw-inset-ring-color: var(--color-lime-600); /* oklch(64.8% 0.2 131.684) */ |
| inset-ring-lime-700 | --tw-inset-ring-color: var(--color-lime-700); /* oklch(53.2% 0.157 131.589) */ |
| inset-ring-lime-800 | --tw-inset-ring-color: var(--color-lime-800); /* oklch(45.3% 0.124 130.933) */ |
| inset-ring-lime-900 | --tw-inset-ring-color: var(--color-lime-900); /* oklch(40.5% 0.101 131.063) */ |
| inset-ring-lime-950 | --tw-inset-ring-color: var(--color-lime-950); /* oklch(27.4% 0.072 132.109) */ |
| inset-ring-green-50 | --tw-inset-ring-color: var(--color-green-50); /* oklch(98.2% 0.018 155.826) */ |
| inset-ring-green-100 | --tw-inset-ring-color: var(--color-green-100); /* oklch(96.2% 0.044 156.743) */ |
| inset-ring-green-200 | --tw-inset-ring-color: var(--color-green-200); /* oklch(92.5% 0.084 155.995) */ |
| inset-ring-green-300 | --tw-inset-ring-color: var(--color-green-300); /* oklch(87.1% 0.15 154.449) */ |
| inset-ring-green-400 | --tw-inset-ring-color: var(--color-green-400); /* oklch(79.2% 0.209 151.711) */ |
| inset-ring-green-500 | --tw-inset-ring-color: var(--color-green-500); /* oklch(72.3% 0.219 149.579) */ |
| inset-ring-green-600 | --tw-inset-ring-color: var(--color-green-600); /* oklch(62.7% 0.194 149.214) */ |
| inset-ring-green-700 | --tw-inset-ring-color: var(--color-green-700); /* oklch(52.7% 0.154 150.069) */ |
| inset-ring-green-800 | --tw-inset-ring-color: var(--color-green-800); /* oklch(44.8% 0.119 151.328) */ |
| inset-ring-green-900 | --tw-inset-ring-color: var(--color-green-900); /* oklch(39.3% 0.095 152.535) */ |
| inset-ring-green-950 | --tw-inset-ring-color: var(--color-green-950); /* oklch(26.6% 0.065 152.934) */ |
| inset-ring-emerald-50 | --tw-inset-ring-color: var(--color-emerald-50); /* oklch(97.9% 0.021 166.113) */ |
| inset-ring-emerald-100 | --tw-inset-ring-color: var(--color-emerald-100); /* oklch(95% 0.052 163.051) */ |
| inset-ring-emerald-200 | --tw-inset-ring-color: var(--color-emerald-200); /* oklch(90.5% 0.093 164.15) */ |
| inset-ring-emerald-300 | --tw-inset-ring-color: var(--color-emerald-300); /* oklch(84.5% 0.143 164.978) */ |
| inset-ring-emerald-400 | --tw-inset-ring-color: var(--color-emerald-400); /* oklch(76.5% 0.177 163.223) */ |
| inset-ring-emerald-500 | --tw-inset-ring-color: var(--color-emerald-500); /* oklch(69.6% 0.17 162.48) */ |
| inset-ring-emerald-600 | --tw-inset-ring-color: var(--color-emerald-600); /* oklch(59.6% 0.145 163.225) */ |
| inset-ring-emerald-700 | --tw-inset-ring-color: var(--color-emerald-700); /* oklch(50.8% 0.118 165.612) */ |
| inset-ring-emerald-800 | --tw-inset-ring-color: var(--color-emerald-800); /* oklch(43.2% 0.095 166.913) */ |
| inset-ring-emerald-900 | --tw-inset-ring-color: var(--color-emerald-900); /* oklch(37.8% 0.077 168.94) */ |
| inset-ring-emerald-950 | --tw-inset-ring-color: var(--color-emerald-950); /* oklch(26.2% 0.051 172.552) */ |
| inset-ring-teal-50 | --tw-inset-ring-color: var(--color-teal-50); /* oklch(98.4% 0.014 180.72) */ |
| inset-ring-teal-100 | --tw-inset-ring-color: var(--color-teal-100); /* oklch(95.3% 0.051 180.801) */ |
| inset-ring-teal-200 | --tw-inset-ring-color: var(--color-teal-200); /* oklch(91% 0.096 180.426) */ |
| inset-ring-teal-300 | --tw-inset-ring-color: var(--color-teal-300); /* oklch(85.5% 0.138 181.071) */ |
| inset-ring-teal-400 | --tw-inset-ring-color: var(--color-teal-400); /* oklch(77.7% 0.152 181.912) */ |
| inset-ring-teal-500 | --tw-inset-ring-color: var(--color-teal-500); /* oklch(70.4% 0.14 182.503) */ |
| inset-ring-teal-600 | --tw-inset-ring-color: var(--color-teal-600); /* oklch(60% 0.118 184.704) */ |
| inset-ring-teal-700 | --tw-inset-ring-color: var(--color-teal-700); /* oklch(51.1% 0.096 186.391) */ |
| inset-ring-teal-800 | --tw-inset-ring-color: var(--color-teal-800); /* oklch(43.7% 0.078 188.216) */ |
| inset-ring-teal-900 | --tw-inset-ring-color: var(--color-teal-900); /* oklch(38.6% 0.063 188.416) */ |
| inset-ring-teal-950 | --tw-inset-ring-color: var(--color-teal-950); /* oklch(27.7% 0.046 192.524) */ |
| inset-ring-cyan-50 | --tw-inset-ring-color: var(--color-cyan-50); /* oklch(98.4% 0.019 200.873) */ |
| inset-ring-cyan-100 | --tw-inset-ring-color: var(--color-cyan-100); /* oklch(95.6% 0.045 203.388) */ |
| inset-ring-cyan-200 | --tw-inset-ring-color: var(--color-cyan-200); /* oklch(91.7% 0.08 205.041) */ |
| inset-ring-cyan-300 | --tw-inset-ring-color: var(--color-cyan-300); /* oklch(86.5% 0.127 207.078) */ |
| inset-ring-cyan-400 | --tw-inset-ring-color: var(--color-cyan-400); /* oklch(78.9% 0.154 211.53) */ |
| inset-ring-cyan-500 | --tw-inset-ring-color: var(--color-cyan-500); /* oklch(71.5% 0.143 215.221) */ |
| inset-ring-cyan-600 | --tw-inset-ring-color: var(--color-cyan-600); /* oklch(60.9% 0.126 221.723) */ |
| inset-ring-cyan-700 | --tw-inset-ring-color: var(--color-cyan-700); /* oklch(52% 0.105 223.128) */ |
| inset-ring-cyan-800 | --tw-inset-ring-color: var(--color-cyan-800); /* oklch(45% 0.085 224.283) */ |
| inset-ring-cyan-900 | --tw-inset-ring-color: var(--color-cyan-900); /* oklch(39.8% 0.07 227.392) */ |
| inset-ring-cyan-950 | --tw-inset-ring-color: var(--color-cyan-950); /* oklch(30.2% 0.056 229.695) */ |
| inset-ring-sky-50 | --tw-inset-ring-color: var(--color-sky-50); /* oklch(97.7% 0.013 236.62) */ |
| inset-ring-sky-100 | --tw-inset-ring-color: var(--color-sky-100); /* oklch(95.1% 0.026 236.824) */ |
| inset-ring-sky-200 | --tw-inset-ring-color: var(--color-sky-200); /* oklch(90.1% 0.058 230.902) */ |
| inset-ring-sky-300 | --tw-inset-ring-color: var(--color-sky-300); /* oklch(82.8% 0.111 230.318) */ |
| inset-ring-sky-400 | --tw-inset-ring-color: var(--color-sky-400); /* oklch(74.6% 0.16 232.661) */ |
| inset-ring-sky-500 | --tw-inset-ring-color: var(--color-sky-500); /* oklch(68.5% 0.169 237.323) */ |
| inset-ring-sky-600 | --tw-inset-ring-color: var(--color-sky-600); /* oklch(58.8% 0.158 241.966) */ |
| inset-ring-sky-700 | --tw-inset-ring-color: var(--color-sky-700); /* oklch(50% 0.134 242.749) */ |
| inset-ring-sky-800 | --tw-inset-ring-color: var(--color-sky-800); /* oklch(44.3% 0.11 240.79) */ |
| inset-ring-sky-900 | --tw-inset-ring-color: var(--color-sky-900); /* oklch(39.1% 0.09 240.876) */ |
| inset-ring-sky-950 | --tw-inset-ring-color: var(--color-sky-950); /* oklch(29.3% 0.066 243.157) */ |
| inset-ring-blue-50 | --tw-inset-ring-color: var(--color-blue-50); /* oklch(97% 0.014 254.604) */ |
| inset-ring-blue-100 | --tw-inset-ring-color: var(--color-blue-100); /* oklch(93.2% 0.032 255.585) */ |
| inset-ring-blue-200 | --tw-inset-ring-color: var(--color-blue-200); /* oklch(88.2% 0.059 254.128) */ |
| inset-ring-blue-300 | --tw-inset-ring-color: var(--color-blue-300); /* oklch(80.9% 0.105 251.813) */ |
| inset-ring-blue-400 | --tw-inset-ring-color: var(--color-blue-400); /* oklch(70.7% 0.165 254.624) */ |
| inset-ring-blue-500 | --tw-inset-ring-color: var(--color-blue-500); /* oklch(62.3% 0.214 259.815) */ |
| inset-ring-blue-600 | --tw-inset-ring-color: var(--color-blue-600); /* oklch(54.6% 0.245 262.881) */ |
| inset-ring-blue-700 | --tw-inset-ring-color: var(--color-blue-700); /* oklch(48.8% 0.243 264.376) */ |
| inset-ring-blue-800 | --tw-inset-ring-color: var(--color-blue-800); /* oklch(42.4% 0.199 265.638) */ |
| inset-ring-blue-900 | --tw-inset-ring-color: var(--color-blue-900); /* oklch(37.9% 0.146 265.522) */ |
| inset-ring-blue-950 | --tw-inset-ring-color: var(--color-blue-950); /* oklch(28.2% 0.091 267.935) */ |
| inset-ring-indigo-50 | --tw-inset-ring-color: var(--color-indigo-50); /* oklch(96.2% 0.018 272.314) */ |
| inset-ring-indigo-100 | --tw-inset-ring-color: var(--color-indigo-100); /* oklch(93% 0.034 272.788) */ |
| inset-ring-indigo-200 | --tw-inset-ring-color: var(--color-indigo-200); /* oklch(87% 0.065 274.039) */ |
| inset-ring-indigo-300 | --tw-inset-ring-color: var(--color-indigo-300); /* oklch(78.5% 0.115 274.713) */ |
| inset-ring-indigo-400 | --tw-inset-ring-color: var(--color-indigo-400); /* oklch(67.3% 0.182 276.935) */ |
| inset-ring-indigo-500 | --tw-inset-ring-color: var(--color-indigo-500); /* oklch(58.5% 0.233 277.117) */ |
| inset-ring-indigo-600 | --tw-inset-ring-color: var(--color-indigo-600); /* oklch(51.1% 0.262 276.966) */ |
| inset-ring-indigo-700 | --tw-inset-ring-color: var(--color-indigo-700); /* oklch(45.7% 0.24 277.023) */ |
| inset-ring-indigo-800 | --tw-inset-ring-color: var(--color-indigo-800); /* oklch(39.8% 0.195 277.366) */ |
| inset-ring-indigo-900 | --tw-inset-ring-color: var(--color-indigo-900); /* oklch(35.9% 0.144 278.697) */ |
| inset-ring-indigo-950 | --tw-inset-ring-color: var(--color-indigo-950); /* oklch(25.7% 0.09 281.288) */ |
| inset-ring-violet-50 | --tw-inset-ring-color: var(--color-violet-50); /* oklch(96.9% 0.016 293.756) */ |
| inset-ring-violet-100 | --tw-inset-ring-color: var(--color-violet-100); /* oklch(94.3% 0.029 294.588) */ |
| inset-ring-violet-200 | --tw-inset-ring-color: var(--color-violet-200); /* oklch(89.4% 0.057 293.283) */ |
| inset-ring-violet-300 | --tw-inset-ring-color: var(--color-violet-300); /* oklch(81.1% 0.111 293.571) */ |
| inset-ring-violet-400 | --tw-inset-ring-color: var(--color-violet-400); /* oklch(70.2% 0.183 293.541) */ |
| inset-ring-violet-500 | --tw-inset-ring-color: var(--color-violet-500); /* oklch(60.6% 0.25 292.717) */ |
| inset-ring-violet-600 | --tw-inset-ring-color: var(--color-violet-600); /* oklch(54.1% 0.281 293.009) */ |
| inset-ring-violet-700 | --tw-inset-ring-color: var(--color-violet-700); /* oklch(49.1% 0.27 292.581) */ |
| inset-ring-violet-800 | --tw-inset-ring-color: var(--color-violet-800); /* oklch(43.2% 0.232 292.759) */ |
| inset-ring-violet-900 | --tw-inset-ring-color: var(--color-violet-900); /* oklch(38% 0.189 293.745) */ |
| inset-ring-violet-950 | --tw-inset-ring-color: var(--color-violet-950); /* oklch(28.3% 0.141 291.089) */ |
| inset-ring-purple-50 | --tw-inset-ring-color: var(--color-purple-50); /* oklch(97.7% 0.014 308.299) */ |
| inset-ring-purple-100 | --tw-inset-ring-color: var(--color-purple-100); /* oklch(94.6% 0.033 307.174) */ |
| inset-ring-purple-200 | --tw-inset-ring-color: var(--color-purple-200); /* oklch(90.2% 0.063 306.703) */ |
| inset-ring-purple-300 | --tw-inset-ring-color: var(--color-purple-300); /* oklch(82.7% 0.119 306.383) */ |
| inset-ring-purple-400 | --tw-inset-ring-color: var(--color-purple-400); /* oklch(71.4% 0.203 305.504) */ |
| inset-ring-purple-500 | --tw-inset-ring-color: var(--color-purple-500); /* oklch(62.7% 0.265 303.9) */ |
| inset-ring-purple-600 | --tw-inset-ring-color: var(--color-purple-600); /* oklch(55.8% 0.288 302.321) */ |
| inset-ring-purple-700 | --tw-inset-ring-color: var(--color-purple-700); /* oklch(49.6% 0.265 301.924) */ |
| inset-ring-purple-800 | --tw-inset-ring-color: var(--color-purple-800); /* oklch(43.8% 0.218 303.724) */ |
| inset-ring-purple-900 | --tw-inset-ring-color: var(--color-purple-900); /* oklch(38.1% 0.176 304.987) */ |
| inset-ring-purple-950 | --tw-inset-ring-color: var(--color-purple-950); /* oklch(29.1% 0.149 302.717) */ |
| inset-ring-fuchsia-50 | --tw-inset-ring-color: var(--color-fuchsia-50); /* oklch(97.7% 0.017 320.058) */ |
| inset-ring-fuchsia-100 | --tw-inset-ring-color: var(--color-fuchsia-100); /* oklch(95.2% 0.037 318.852) */ |
| inset-ring-fuchsia-200 | --tw-inset-ring-color: var(--color-fuchsia-200); /* oklch(90.3% 0.076 319.62) */ |
| inset-ring-fuchsia-300 | --tw-inset-ring-color: var(--color-fuchsia-300); /* oklch(83.3% 0.145 321.434) */ |
| inset-ring-fuchsia-400 | --tw-inset-ring-color: var(--color-fuchsia-400); /* oklch(74% 0.238 322.16) */ |
| inset-ring-fuchsia-500 | --tw-inset-ring-color: var(--color-fuchsia-500); /* oklch(66.7% 0.295 322.15) */ |
| inset-ring-fuchsia-600 | --tw-inset-ring-color: var(--color-fuchsia-600); /* oklch(59.1% 0.293 322.896) */ |
| inset-ring-fuchsia-700 | --tw-inset-ring-color: var(--color-fuchsia-700); /* oklch(51.8% 0.253 323.949) */ |
| inset-ring-fuchsia-800 | --tw-inset-ring-color: var(--color-fuchsia-800); /* oklch(45.2% 0.211 324.591) */ |
| inset-ring-fuchsia-900 | --tw-inset-ring-color: var(--color-fuchsia-900); /* oklch(40.1% 0.17 325.612) */ |
| inset-ring-fuchsia-950 | --tw-inset-ring-color: var(--color-fuchsia-950); /* oklch(29.3% 0.136 325.661) */ |
| inset-ring-pink-50 | --tw-inset-ring-color: var(--color-pink-50); /* oklch(97.1% 0.014 343.198) */ |
| inset-ring-pink-100 | --tw-inset-ring-color: var(--color-pink-100); /* oklch(94.8% 0.028 342.258) */ |
| inset-ring-pink-200 | --tw-inset-ring-color: var(--color-pink-200); /* oklch(89.9% 0.061 343.231) */ |
| inset-ring-pink-300 | --tw-inset-ring-color: var(--color-pink-300); /* oklch(82.3% 0.12 346.018) */ |
| inset-ring-pink-400 | --tw-inset-ring-color: var(--color-pink-400); /* oklch(71.8% 0.202 349.761) */ |
| inset-ring-pink-500 | --tw-inset-ring-color: var(--color-pink-500); /* oklch(65.6% 0.241 354.308) */ |
| inset-ring-pink-600 | --tw-inset-ring-color: var(--color-pink-600); /* oklch(59.2% 0.249 0.584) */ |
| inset-ring-pink-700 | --tw-inset-ring-color: var(--color-pink-700); /* oklch(52.5% 0.223 3.958) */ |
| inset-ring-pink-800 | --tw-inset-ring-color: var(--color-pink-800); /* oklch(45.9% 0.187 3.815) */ |
| inset-ring-pink-900 | --tw-inset-ring-color: var(--color-pink-900); /* oklch(40.8% 0.153 2.432) */ |
| inset-ring-pink-950 | --tw-inset-ring-color: var(--color-pink-950); /* oklch(28.4% 0.109 3.907) */ |
| inset-ring-rose-50 | --tw-inset-ring-color: var(--color-rose-50); /* oklch(96.9% 0.015 12.422) */ |
| inset-ring-rose-100 | --tw-inset-ring-color: var(--color-rose-100); /* oklch(94.1% 0.03 12.58) */ |
| inset-ring-rose-200 | --tw-inset-ring-color: var(--color-rose-200); /* oklch(89.2% 0.058 10.001) */ |
| inset-ring-rose-300 | --tw-inset-ring-color: var(--color-rose-300); /* oklch(81% 0.117 11.638) */ |
| inset-ring-rose-400 | --tw-inset-ring-color: var(--color-rose-400); /* oklch(71.2% 0.194 13.428) */ |
| inset-ring-rose-500 | --tw-inset-ring-color: var(--color-rose-500); /* oklch(64.5% 0.246 16.439) */ |
| inset-ring-rose-600 | --tw-inset-ring-color: var(--color-rose-600); /* oklch(58.6% 0.253 17.585) */ |
| inset-ring-rose-700 | --tw-inset-ring-color: var(--color-rose-700); /* oklch(51.4% 0.222 16.935) */ |
| inset-ring-rose-800 | --tw-inset-ring-color: var(--color-rose-800); /* oklch(45.5% 0.188 13.697) */ |
| inset-ring-rose-900 | --tw-inset-ring-color: var(--color-rose-900); /* oklch(41% 0.159 10.272) */ |
| inset-ring-rose-950 | --tw-inset-ring-color: var(--color-rose-950); /* oklch(27.1% 0.105 12.094) */ |
| inset-ring-slate-50 | --tw-inset-ring-color: var(--color-slate-50); /* oklch(98.4% 0.003 247.858) */ |
| inset-ring-slate-100 | --tw-inset-ring-color: var(--color-slate-100); /* oklch(96.8% 0.007 247.896) */ |
| inset-ring-slate-200 | --tw-inset-ring-color: var(--color-slate-200); /* oklch(92.9% 0.013 255.508) */ |
| inset-ring-slate-300 | --tw-inset-ring-color: var(--color-slate-300); /* oklch(86.9% 0.022 252.894) */ |
| inset-ring-slate-400 | --tw-inset-ring-color: var(--color-slate-400); /* oklch(70.4% 0.04 256.788) */ |
| inset-ring-slate-500 | --tw-inset-ring-color: var(--color-slate-500); /* oklch(55.4% 0.046 257.417) */ |
| inset-ring-slate-600 | --tw-inset-ring-color: var(--color-slate-600); /* oklch(44.6% 0.043 257.281) */ |
| inset-ring-slate-700 | --tw-inset-ring-color: var(--color-slate-700); /* oklch(37.2% 0.044 257.287) */ |
| inset-ring-slate-800 | --tw-inset-ring-color: var(--color-slate-800); /* oklch(27.9% 0.041 260.031) */ |
| inset-ring-slate-900 | --tw-inset-ring-color: var(--color-slate-900); /* oklch(20.8% 0.042 265.755) */ |
| inset-ring-slate-950 | --tw-inset-ring-color: var(--color-slate-950); /* oklch(12.9% 0.042 264.695) */ |
| inset-ring-gray-50 | --tw-inset-ring-color: var(--color-gray-50); /* oklch(98.5% 0.002 247.839) */ |
| inset-ring-gray-100 | --tw-inset-ring-color: var(--color-gray-100); /* oklch(96.7% 0.003 264.542) */ |
| inset-ring-gray-200 | --tw-inset-ring-color: var(--color-gray-200); /* oklch(92.8% 0.006 264.531) */ |
| inset-ring-gray-300 | --tw-inset-ring-color: var(--color-gray-300); /* oklch(87.2% 0.01 258.338) */ |
| inset-ring-gray-400 | --tw-inset-ring-color: var(--color-gray-400); /* oklch(70.7% 0.022 261.325) */ |
| inset-ring-gray-500 | --tw-inset-ring-color: var(--color-gray-500); /* oklch(55.1% 0.027 264.364) */ |
| inset-ring-gray-600 | --tw-inset-ring-color: var(--color-gray-600); /* oklch(44.6% 0.03 256.802) */ |
| inset-ring-gray-700 | --tw-inset-ring-color: var(--color-gray-700); /* oklch(37.3% 0.034 259.733) */ |
| inset-ring-gray-800 | --tw-inset-ring-color: var(--color-gray-800); /* oklch(27.8% 0.033 256.848) */ |
| inset-ring-gray-900 | --tw-inset-ring-color: var(--color-gray-900); /* oklch(21% 0.034 264.665) */ |
| inset-ring-gray-950 | --tw-inset-ring-color: var(--color-gray-950); /* oklch(13% 0.028 261.692) */ |
| inset-ring-zinc-50 | --tw-inset-ring-color: var(--color-zinc-50); /* oklch(98.5% 0 0) */ |
| inset-ring-zinc-100 | --tw-inset-ring-color: var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */ |
| inset-ring-zinc-200 | --tw-inset-ring-color: var(--color-zinc-200); /* oklch(92% 0.004 286.32) */ |
| inset-ring-zinc-300 | --tw-inset-ring-color: var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */ |
| inset-ring-zinc-400 | --tw-inset-ring-color: var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */ |
| inset-ring-zinc-500 | --tw-inset-ring-color: var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */ |
| inset-ring-zinc-600 | --tw-inset-ring-color: var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */ |
| inset-ring-zinc-700 | --tw-inset-ring-color: var(--color-zinc-700); /* oklch(37% 0.013 285.805) */ |
| inset-ring-zinc-800 | --tw-inset-ring-color: var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */ |
| inset-ring-zinc-900 | --tw-inset-ring-color: var(--color-zinc-900); /* oklch(21% 0.006 285.885) */ |
| inset-ring-zinc-950 | --tw-inset-ring-color: var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */ |
| inset-ring-neutral-50 | --tw-inset-ring-color: var(--color-neutral-50); /* oklch(98.5% 0 0) */ |
| inset-ring-neutral-100 | --tw-inset-ring-color: var(--color-neutral-100); /* oklch(97% 0 0) */ |
| inset-ring-neutral-200 | --tw-inset-ring-color: var(--color-neutral-200); /* oklch(92.2% 0 0) */ |
| inset-ring-neutral-300 | --tw-inset-ring-color: var(--color-neutral-300); /* oklch(87% 0 0) */ |
| inset-ring-neutral-400 | --tw-inset-ring-color: var(--color-neutral-400); /* oklch(70.8% 0 0) */ |
| inset-ring-neutral-500 | --tw-inset-ring-color: var(--color-neutral-500); /* oklch(55.6% 0 0) */ |
| inset-ring-neutral-600 | --tw-inset-ring-color: var(--color-neutral-600); /* oklch(43.9% 0 0) */ |
| inset-ring-neutral-700 | --tw-inset-ring-color: var(--color-neutral-700); /* oklch(37.1% 0 0) */ |
| inset-ring-neutral-800 | --tw-inset-ring-color: var(--color-neutral-800); /* oklch(26.9% 0 0) */ |
| inset-ring-neutral-900 | --tw-inset-ring-color: var(--color-neutral-900); /* oklch(20.5% 0 0) */ |
| inset-ring-neutral-950 | --tw-inset-ring-color: var(--color-neutral-950); /* oklch(14.5% 0 0) */ |
| inset-ring-stone-50 | --tw-inset-ring-color: var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */ |
| inset-ring-stone-100 | --tw-inset-ring-color: var(--color-stone-100); /* oklch(97% 0.001 106.424) */ |
| inset-ring-stone-200 | --tw-inset-ring-color: var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */ |
| inset-ring-stone-300 | --tw-inset-ring-color: var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */ |
| inset-ring-stone-400 | --tw-inset-ring-color: var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */ |
| inset-ring-stone-500 | --tw-inset-ring-color: var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */ |
| inset-ring-stone-600 | --tw-inset-ring-color: var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */ |
| inset-ring-stone-700 | --tw-inset-ring-color: var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */ |
| inset-ring-stone-800 | --tw-inset-ring-color: var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */ |
| inset-ring-stone-900 | --tw-inset-ring-color: var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */ |
| inset-ring-stone-950 | --tw-inset-ring-color: var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */ |

[Documentation](https://tailwindcss.com/docs/box-shadow)

---

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
| text-shadow-(<custom-property>) | text-shadow: var(<custom-property>); |
| text-shadow-(color:<custom-property>) | --tw-shadow-color var(<custom-property>); |
| text-shadow-[<value>] | text-shadow: <value>; |
| text-shadow-inherit | --tw-shadow-color inherit; |
| text-shadow-current | --tw-shadow-color currentColor; |
| text-shadow-transparent | --tw-shadow-color transparent; |
| text-shadow-black | --tw-text-shadow-color var(--color-black); /* #000 */ |
| text-shadow-white | --tw-text-shadow-color var(--color-white); /* #fff */ |
| text-shadow-red-50 | --tw-text-shadow-color var(--color-red-50); /* oklch(97.1% 0.013 17.38) */ |
| text-shadow-red-100 | --tw-text-shadow-color var(--color-red-100); /* oklch(93.6% 0.032 17.717) */ |
| text-shadow-red-200 | --tw-text-shadow-color var(--color-red-200); /* oklch(88.5% 0.062 18.334) */ |
| text-shadow-red-300 | --tw-text-shadow-color var(--color-red-300); /* oklch(80.8% 0.114 19.571) */ |
| text-shadow-red-400 | --tw-text-shadow-color var(--color-red-400); /* oklch(70.4% 0.191 22.216) */ |
| text-shadow-red-500 | --tw-text-shadow-color var(--color-red-500); /* oklch(63.7% 0.237 25.331) */ |
| text-shadow-red-600 | --tw-text-shadow-color var(--color-red-600); /* oklch(57.7% 0.245 27.325) */ |
| text-shadow-red-700 | --tw-text-shadow-color var(--color-red-700); /* oklch(50.5% 0.213 27.518) */ |
| text-shadow-red-800 | --tw-text-shadow-color var(--color-red-800); /* oklch(44.4% 0.177 26.899) */ |
| text-shadow-red-900 | --tw-text-shadow-color var(--color-red-900); /* oklch(39.6% 0.141 25.723) */ |
| text-shadow-red-950 | --tw-text-shadow-color var(--color-red-950); /* oklch(25.8% 0.092 26.042) */ |
| text-shadow-orange-50 | --tw-text-shadow-color var(--color-orange-50); /* oklch(98% 0.016 73.684) */ |
| text-shadow-orange-100 | --tw-text-shadow-color var(--color-orange-100); /* oklch(95.4% 0.038 75.164) */ |
| text-shadow-orange-200 | --tw-text-shadow-color var(--color-orange-200); /* oklch(90.1% 0.076 70.697) */ |
| text-shadow-orange-300 | --tw-text-shadow-color var(--color-orange-300); /* oklch(83.7% 0.128 66.29) */ |
| text-shadow-orange-400 | --tw-text-shadow-color var(--color-orange-400); /* oklch(75% 0.183 55.934) */ |
| text-shadow-orange-500 | --tw-text-shadow-color var(--color-orange-500); /* oklch(70.5% 0.213 47.604) */ |
| text-shadow-orange-600 | --tw-text-shadow-color var(--color-orange-600); /* oklch(64.6% 0.222 41.116) */ |
| text-shadow-orange-700 | --tw-text-shadow-color var(--color-orange-700); /* oklch(55.3% 0.195 38.402) */ |
| text-shadow-orange-800 | --tw-text-shadow-color var(--color-orange-800); /* oklch(47% 0.157 37.304) */ |
| text-shadow-orange-900 | --tw-text-shadow-color var(--color-orange-900); /* oklch(40.8% 0.123 38.172) */ |
| text-shadow-orange-950 | --tw-text-shadow-color var(--color-orange-950); /* oklch(26.6% 0.079 36.259) */ |
| text-shadow-amber-50 | --tw-text-shadow-color var(--color-amber-50); /* oklch(98.7% 0.022 95.277) */ |
| text-shadow-amber-100 | --tw-text-shadow-color var(--color-amber-100); /* oklch(96.2% 0.059 95.617) */ |
| text-shadow-amber-200 | --tw-text-shadow-color var(--color-amber-200); /* oklch(92.4% 0.12 95.746) */ |
| text-shadow-amber-300 | --tw-text-shadow-color var(--color-amber-300); /* oklch(87.9% 0.169 91.605) */ |
| text-shadow-amber-400 | --tw-text-shadow-color var(--color-amber-400); /* oklch(82.8% 0.189 84.429) */ |
| text-shadow-amber-500 | --tw-text-shadow-color var(--color-amber-500); /* oklch(76.9% 0.188 70.08) */ |
| text-shadow-amber-600 | --tw-text-shadow-color var(--color-amber-600); /* oklch(66.6% 0.179 58.318) */ |
| text-shadow-amber-700 | --tw-text-shadow-color var(--color-amber-700); /* oklch(55.5% 0.163 48.998) */ |
| text-shadow-amber-800 | --tw-text-shadow-color var(--color-amber-800); /* oklch(47.3% 0.137 46.201) */ |
| text-shadow-amber-900 | --tw-text-shadow-color var(--color-amber-900); /* oklch(41.4% 0.112 45.904) */ |
| text-shadow-amber-950 | --tw-text-shadow-color var(--color-amber-950); /* oklch(27.9% 0.077 45.635) */ |
| text-shadow-yellow-50 | --tw-text-shadow-color var(--color-yellow-50); /* oklch(98.7% 0.026 102.212) */ |
| text-shadow-yellow-100 | --tw-text-shadow-color var(--color-yellow-100); /* oklch(97.3% 0.071 103.193) */ |
| text-shadow-yellow-200 | --tw-text-shadow-color var(--color-yellow-200); /* oklch(94.5% 0.129 101.54) */ |
| text-shadow-yellow-300 | --tw-text-shadow-color var(--color-yellow-300); /* oklch(90.5% 0.182 98.111) */ |
| text-shadow-yellow-400 | --tw-text-shadow-color var(--color-yellow-400); /* oklch(85.2% 0.199 91.936) */ |
| text-shadow-yellow-500 | --tw-text-shadow-color var(--color-yellow-500); /* oklch(79.5% 0.184 86.047) */ |
| text-shadow-yellow-600 | --tw-text-shadow-color var(--color-yellow-600); /* oklch(68.1% 0.162 75.834) */ |
| text-shadow-yellow-700 | --tw-text-shadow-color var(--color-yellow-700); /* oklch(55.4% 0.135 66.442) */ |
| text-shadow-yellow-800 | --tw-text-shadow-color var(--color-yellow-800); /* oklch(47.6% 0.114 61.907) */ |
| text-shadow-yellow-900 | --tw-text-shadow-color var(--color-yellow-900); /* oklch(42.1% 0.095 57.708) */ |
| text-shadow-yellow-950 | --tw-text-shadow-color var(--color-yellow-950); /* oklch(28.6% 0.066 53.813) */ |
| text-shadow-lime-50 | --tw-text-shadow-color var(--color-lime-50); /* oklch(98.6% 0.031 120.757) */ |
| text-shadow-lime-100 | --tw-text-shadow-color var(--color-lime-100); /* oklch(96.7% 0.067 122.328) */ |
| text-shadow-lime-200 | --tw-text-shadow-color var(--color-lime-200); /* oklch(93.8% 0.127 124.321) */ |
| text-shadow-lime-300 | --tw-text-shadow-color var(--color-lime-300); /* oklch(89.7% 0.196 126.665) */ |
| text-shadow-lime-400 | --tw-text-shadow-color var(--color-lime-400); /* oklch(84.1% 0.238 128.85) */ |
| text-shadow-lime-500 | --tw-text-shadow-color var(--color-lime-500); /* oklch(76.8% 0.233 130.85) */ |
| text-shadow-lime-600 | --tw-text-shadow-color var(--color-lime-600); /* oklch(64.8% 0.2 131.684) */ |
| text-shadow-lime-700 | --tw-text-shadow-color var(--color-lime-700); /* oklch(53.2% 0.157 131.589) */ |
| text-shadow-lime-800 | --tw-text-shadow-color var(--color-lime-800); /* oklch(45.3% 0.124 130.933) */ |
| text-shadow-lime-900 | --tw-text-shadow-color var(--color-lime-900); /* oklch(40.5% 0.101 131.063) */ |
| text-shadow-lime-950 | --tw-text-shadow-color var(--color-lime-950); /* oklch(27.4% 0.072 132.109) */ |
| text-shadow-green-50 | --tw-text-shadow-color var(--color-green-50); /* oklch(98.2% 0.018 155.826) */ |
| text-shadow-green-100 | --tw-text-shadow-color var(--color-green-100); /* oklch(96.2% 0.044 156.743) */ |
| text-shadow-green-200 | --tw-text-shadow-color var(--color-green-200); /* oklch(92.5% 0.084 155.995) */ |
| text-shadow-green-300 | --tw-text-shadow-color var(--color-green-300); /* oklch(87.1% 0.15 154.449) */ |
| text-shadow-green-400 | --tw-text-shadow-color var(--color-green-400); /* oklch(79.2% 0.209 151.711) */ |
| text-shadow-green-500 | --tw-text-shadow-color var(--color-green-500); /* oklch(72.3% 0.219 149.579) */ |
| text-shadow-green-600 | --tw-text-shadow-color var(--color-green-600); /* oklch(62.7% 0.194 149.214) */ |
| text-shadow-green-700 | --tw-text-shadow-color var(--color-green-700); /* oklch(52.7% 0.154 150.069) */ |
| text-shadow-green-800 | --tw-text-shadow-color var(--color-green-800); /* oklch(44.8% 0.119 151.328) */ |
| text-shadow-green-900 | --tw-text-shadow-color var(--color-green-900); /* oklch(39.3% 0.095 152.535) */ |
| text-shadow-green-950 | --tw-text-shadow-color var(--color-green-950); /* oklch(26.6% 0.065 152.934) */ |
| text-shadow-emerald-50 | --tw-text-shadow-color var(--color-emerald-50); /* oklch(97.9% 0.021 166.113) */ |
| text-shadow-emerald-100 | --tw-text-shadow-color var(--color-emerald-100); /* oklch(95% 0.052 163.051) */ |
| text-shadow-emerald-200 | --tw-text-shadow-color var(--color-emerald-200); /* oklch(90.5% 0.093 164.15) */ |
| text-shadow-emerald-300 | --tw-text-shadow-color var(--color-emerald-300); /* oklch(84.5% 0.143 164.978) */ |
| text-shadow-emerald-400 | --tw-text-shadow-color var(--color-emerald-400); /* oklch(76.5% 0.177 163.223) */ |
| text-shadow-emerald-500 | --tw-text-shadow-color var(--color-emerald-500); /* oklch(69.6% 0.17 162.48) */ |
| text-shadow-emerald-600 | --tw-text-shadow-color var(--color-emerald-600); /* oklch(59.6% 0.145 163.225) */ |
| text-shadow-emerald-700 | --tw-text-shadow-color var(--color-emerald-700); /* oklch(50.8% 0.118 165.612) */ |
| text-shadow-emerald-800 | --tw-text-shadow-color var(--color-emerald-800); /* oklch(43.2% 0.095 166.913) */ |
| text-shadow-emerald-900 | --tw-text-shadow-color var(--color-emerald-900); /* oklch(37.8% 0.077 168.94) */ |
| text-shadow-emerald-950 | --tw-text-shadow-color var(--color-emerald-950); /* oklch(26.2% 0.051 172.552) */ |
| text-shadow-teal-50 | --tw-text-shadow-color var(--color-teal-50); /* oklch(98.4% 0.014 180.72) */ |
| text-shadow-teal-100 | --tw-text-shadow-color var(--color-teal-100); /* oklch(95.3% 0.051 180.801) */ |
| text-shadow-teal-200 | --tw-text-shadow-color var(--color-teal-200); /* oklch(91% 0.096 180.426) */ |
| text-shadow-teal-300 | --tw-text-shadow-color var(--color-teal-300); /* oklch(85.5% 0.138 181.071) */ |
| text-shadow-teal-400 | --tw-text-shadow-color var(--color-teal-400); /* oklch(77.7% 0.152 181.912) */ |
| text-shadow-teal-500 | --tw-text-shadow-color var(--color-teal-500); /* oklch(70.4% 0.14 182.503) */ |
| text-shadow-teal-600 | --tw-text-shadow-color var(--color-teal-600); /* oklch(60% 0.118 184.704) */ |
| text-shadow-teal-700 | --tw-text-shadow-color var(--color-teal-700); /* oklch(51.1% 0.096 186.391) */ |
| text-shadow-teal-800 | --tw-text-shadow-color var(--color-teal-800); /* oklch(43.7% 0.078 188.216) */ |
| text-shadow-teal-900 | --tw-text-shadow-color var(--color-teal-900); /* oklch(38.6% 0.063 188.416) */ |
| text-shadow-teal-950 | --tw-text-shadow-color var(--color-teal-950); /* oklch(27.7% 0.046 192.524) */ |
| text-shadow-cyan-50 | --tw-text-shadow-color var(--color-cyan-50); /* oklch(98.4% 0.019 200.873) */ |
| text-shadow-cyan-100 | --tw-text-shadow-color var(--color-cyan-100); /* oklch(95.6% 0.045 203.388) */ |
| text-shadow-cyan-200 | --tw-text-shadow-color var(--color-cyan-200); /* oklch(91.7% 0.08 205.041) */ |
| text-shadow-cyan-300 | --tw-text-shadow-color var(--color-cyan-300); /* oklch(86.5% 0.127 207.078) */ |
| text-shadow-cyan-400 | --tw-text-shadow-color var(--color-cyan-400); /* oklch(78.9% 0.154 211.53) */ |
| text-shadow-cyan-500 | --tw-text-shadow-color var(--color-cyan-500); /* oklch(71.5% 0.143 215.221) */ |
| text-shadow-cyan-600 | --tw-text-shadow-color var(--color-cyan-600); /* oklch(60.9% 0.126 221.723) */ |
| text-shadow-cyan-700 | --tw-text-shadow-color var(--color-cyan-700); /* oklch(52% 0.105 223.128) */ |
| text-shadow-cyan-800 | --tw-text-shadow-color var(--color-cyan-800); /* oklch(45% 0.085 224.283) */ |
| text-shadow-cyan-900 | --tw-text-shadow-color var(--color-cyan-900); /* oklch(39.8% 0.07 227.392) */ |
| text-shadow-cyan-950 | --tw-text-shadow-color var(--color-cyan-950); /* oklch(30.2% 0.056 229.695) */ |
| text-shadow-sky-50 | --tw-text-shadow-color var(--color-sky-50); /* oklch(97.7% 0.013 236.62) */ |
| text-shadow-sky-100 | --tw-text-shadow-color var(--color-sky-100); /* oklch(95.1% 0.026 236.824) */ |
| text-shadow-sky-200 | --tw-text-shadow-color var(--color-sky-200); /* oklch(90.1% 0.058 230.902) */ |
| text-shadow-sky-300 | --tw-text-shadow-color var(--color-sky-300); /* oklch(82.8% 0.111 230.318) */ |
| text-shadow-sky-400 | --tw-text-shadow-color var(--color-sky-400); /* oklch(74.6% 0.16 232.661) */ |
| text-shadow-sky-500 | --tw-text-shadow-color var(--color-sky-500); /* oklch(68.5% 0.169 237.323) */ |
| text-shadow-sky-600 | --tw-text-shadow-color var(--color-sky-600); /* oklch(58.8% 0.158 241.966) */ |
| text-shadow-sky-700 | --tw-text-shadow-color var(--color-sky-700); /* oklch(50% 0.134 242.749) */ |
| text-shadow-sky-800 | --tw-text-shadow-color var(--color-sky-800); /* oklch(44.3% 0.11 240.79) */ |
| text-shadow-sky-900 | --tw-text-shadow-color var(--color-sky-900); /* oklch(39.1% 0.09 240.876) */ |
| text-shadow-sky-950 | --tw-text-shadow-color var(--color-sky-950); /* oklch(29.3% 0.066 243.157) */ |
| text-shadow-blue-50 | --tw-text-shadow-color var(--color-blue-50); /* oklch(97% 0.014 254.604) */ |
| text-shadow-blue-100 | --tw-text-shadow-color var(--color-blue-100); /* oklch(93.2% 0.032 255.585) */ |
| text-shadow-blue-200 | --tw-text-shadow-color var(--color-blue-200); /* oklch(88.2% 0.059 254.128) */ |
| text-shadow-blue-300 | --tw-text-shadow-color var(--color-blue-300); /* oklch(80.9% 0.105 251.813) */ |
| text-shadow-blue-400 | --tw-text-shadow-color var(--color-blue-400); /* oklch(70.7% 0.165 254.624) */ |
| text-shadow-blue-500 | --tw-text-shadow-color var(--color-blue-500); /* oklch(62.3% 0.214 259.815) */ |
| text-shadow-blue-600 | --tw-text-shadow-color var(--color-blue-600); /* oklch(54.6% 0.245 262.881) */ |
| text-shadow-blue-700 | --tw-text-shadow-color var(--color-blue-700); /* oklch(48.8% 0.243 264.376) */ |
| text-shadow-blue-800 | --tw-text-shadow-color var(--color-blue-800); /* oklch(42.4% 0.199 265.638) */ |
| text-shadow-blue-900 | --tw-text-shadow-color var(--color-blue-900); /* oklch(37.9% 0.146 265.522) */ |
| text-shadow-blue-950 | --tw-text-shadow-color var(--color-blue-950); /* oklch(28.2% 0.091 267.935) */ |
| text-shadow-indigo-50 | --tw-text-shadow-color var(--color-indigo-50); /* oklch(96.2% 0.018 272.314) */ |
| text-shadow-indigo-100 | --tw-text-shadow-color var(--color-indigo-100); /* oklch(93% 0.034 272.788) */ |
| text-shadow-indigo-200 | --tw-text-shadow-color var(--color-indigo-200); /* oklch(87% 0.065 274.039) */ |
| text-shadow-indigo-300 | --tw-text-shadow-color var(--color-indigo-300); /* oklch(78.5% 0.115 274.713) */ |
| text-shadow-indigo-400 | --tw-text-shadow-color var(--color-indigo-400); /* oklch(67.3% 0.182 276.935) */ |
| text-shadow-indigo-500 | --tw-text-shadow-color var(--color-indigo-500); /* oklch(58.5% 0.233 277.117) */ |
| text-shadow-indigo-600 | --tw-text-shadow-color var(--color-indigo-600); /* oklch(51.1% 0.262 276.966) */ |
| text-shadow-indigo-700 | --tw-text-shadow-color var(--color-indigo-700); /* oklch(45.7% 0.24 277.023) */ |
| text-shadow-indigo-800 | --tw-text-shadow-color var(--color-indigo-800); /* oklch(39.8% 0.195 277.366) */ |
| text-shadow-indigo-900 | --tw-text-shadow-color var(--color-indigo-900); /* oklch(35.9% 0.144 278.697) */ |
| text-shadow-indigo-950 | --tw-text-shadow-color var(--color-indigo-950); /* oklch(25.7% 0.09 281.288) */ |
| text-shadow-violet-50 | --tw-text-shadow-color var(--color-violet-50); /* oklch(96.9% 0.016 293.756) */ |
| text-shadow-violet-100 | --tw-text-shadow-color var(--color-violet-100); /* oklch(94.3% 0.029 294.588) */ |
| text-shadow-violet-200 | --tw-text-shadow-color var(--color-violet-200); /* oklch(89.4% 0.057 293.283) */ |
| text-shadow-violet-300 | --tw-text-shadow-color var(--color-violet-300); /* oklch(81.1% 0.111 293.571) */ |
| text-shadow-violet-400 | --tw-text-shadow-color var(--color-violet-400); /* oklch(70.2% 0.183 293.541) */ |
| text-shadow-violet-500 | --tw-text-shadow-color var(--color-violet-500); /* oklch(60.6% 0.25 292.717) */ |
| text-shadow-violet-600 | --tw-text-shadow-color var(--color-violet-600); /* oklch(54.1% 0.281 293.009) */ |
| text-shadow-violet-700 | --tw-text-shadow-color var(--color-violet-700); /* oklch(49.1% 0.27 292.581) */ |
| text-shadow-violet-800 | --tw-text-shadow-color var(--color-violet-800); /* oklch(43.2% 0.232 292.759) */ |
| text-shadow-violet-900 | --tw-text-shadow-color var(--color-violet-900); /* oklch(38% 0.189 293.745) */ |
| text-shadow-violet-950 | --tw-text-shadow-color var(--color-violet-950); /* oklch(28.3% 0.141 291.089) */ |
| text-shadow-purple-50 | --tw-text-shadow-color var(--color-purple-50); /* oklch(97.7% 0.014 308.299) */ |
| text-shadow-purple-100 | --tw-text-shadow-color var(--color-purple-100); /* oklch(94.6% 0.033 307.174) */ |
| text-shadow-purple-200 | --tw-text-shadow-color var(--color-purple-200); /* oklch(90.2% 0.063 306.703) */ |
| text-shadow-purple-300 | --tw-text-shadow-color var(--color-purple-300); /* oklch(82.7% 0.119 306.383) */ |
| text-shadow-purple-400 | --tw-text-shadow-color var(--color-purple-400); /* oklch(71.4% 0.203 305.504) */ |
| text-shadow-purple-500 | --tw-text-shadow-color var(--color-purple-500); /* oklch(62.7% 0.265 303.9) */ |
| text-shadow-purple-600 | --tw-text-shadow-color var(--color-purple-600); /* oklch(55.8% 0.288 302.321) */ |
| text-shadow-purple-700 | --tw-text-shadow-color var(--color-purple-700); /* oklch(49.6% 0.265 301.924) */ |
| text-shadow-purple-800 | --tw-text-shadow-color var(--color-purple-800); /* oklch(43.8% 0.218 303.724) */ |
| text-shadow-purple-900 | --tw-text-shadow-color var(--color-purple-900); /* oklch(38.1% 0.176 304.987) */ |
| text-shadow-purple-950 | --tw-text-shadow-color var(--color-purple-950); /* oklch(29.1% 0.149 302.717) */ |
| text-shadow-fuchsia-50 | --tw-text-shadow-color var(--color-fuchsia-50); /* oklch(97.7% 0.017 320.058) */ |
| text-shadow-fuchsia-100 | --tw-text-shadow-color var(--color-fuchsia-100); /* oklch(95.2% 0.037 318.852) */ |
| text-shadow-fuchsia-200 | --tw-text-shadow-color var(--color-fuchsia-200); /* oklch(90.3% 0.076 319.62) */ |
| text-shadow-fuchsia-300 | --tw-text-shadow-color var(--color-fuchsia-300); /* oklch(83.3% 0.145 321.434) */ |
| text-shadow-fuchsia-400 | --tw-text-shadow-color var(--color-fuchsia-400); /* oklch(74% 0.238 322.16) */ |
| text-shadow-fuchsia-500 | --tw-text-shadow-color var(--color-fuchsia-500); /* oklch(66.7% 0.295 322.15) */ |
| text-shadow-fuchsia-600 | --tw-text-shadow-color var(--color-fuchsia-600); /* oklch(59.1% 0.293 322.896) */ |
| text-shadow-fuchsia-700 | --tw-text-shadow-color var(--color-fuchsia-700); /* oklch(51.8% 0.253 323.949) */ |
| text-shadow-fuchsia-800 | --tw-text-shadow-color var(--color-fuchsia-800); /* oklch(45.2% 0.211 324.591) */ |
| text-shadow-fuchsia-900 | --tw-text-shadow-color var(--color-fuchsia-900); /* oklch(40.1% 0.17 325.612) */ |
| text-shadow-fuchsia-950 | --tw-text-shadow-color var(--color-fuchsia-950); /* oklch(29.3% 0.136 325.661) */ |
| text-shadow-pink-50 | --tw-text-shadow-color var(--color-pink-50); /* oklch(97.1% 0.014 343.198) */ |
| text-shadow-pink-100 | --tw-text-shadow-color var(--color-pink-100); /* oklch(94.8% 0.028 342.258) */ |
| text-shadow-pink-200 | --tw-text-shadow-color var(--color-pink-200); /* oklch(89.9% 0.061 343.231) */ |
| text-shadow-pink-300 | --tw-text-shadow-color var(--color-pink-300); /* oklch(82.3% 0.12 346.018) */ |
| text-shadow-pink-400 | --tw-text-shadow-color var(--color-pink-400); /* oklch(71.8% 0.202 349.761) */ |
| text-shadow-pink-500 | --tw-text-shadow-color var(--color-pink-500); /* oklch(65.6% 0.241 354.308) */ |
| text-shadow-pink-600 | --tw-text-shadow-color var(--color-pink-600); /* oklch(59.2% 0.249 0.584) */ |
| text-shadow-pink-700 | --tw-text-shadow-color var(--color-pink-700); /* oklch(52.5% 0.223 3.958) */ |
| text-shadow-pink-800 | --tw-text-shadow-color var(--color-pink-800); /* oklch(45.9% 0.187 3.815) */ |
| text-shadow-pink-900 | --tw-text-shadow-color var(--color-pink-900); /* oklch(40.8% 0.153 2.432) */ |
| text-shadow-pink-950 | --tw-text-shadow-color var(--color-pink-950); /* oklch(28.4% 0.109 3.907) */ |
| text-shadow-rose-50 | --tw-text-shadow-color var(--color-rose-50); /* oklch(96.9% 0.015 12.422) */ |
| text-shadow-rose-100 | --tw-text-shadow-color var(--color-rose-100); /* oklch(94.1% 0.03 12.58) */ |
| text-shadow-rose-200 | --tw-text-shadow-color var(--color-rose-200); /* oklch(89.2% 0.058 10.001) */ |
| text-shadow-rose-300 | --tw-text-shadow-color var(--color-rose-300); /* oklch(81% 0.117 11.638) */ |
| text-shadow-rose-400 | --tw-text-shadow-color var(--color-rose-400); /* oklch(71.2% 0.194 13.428) */ |
| text-shadow-rose-500 | --tw-text-shadow-color var(--color-rose-500); /* oklch(64.5% 0.246 16.439) */ |
| text-shadow-rose-600 | --tw-text-shadow-color var(--color-rose-600); /* oklch(58.6% 0.253 17.585) */ |
| text-shadow-rose-700 | --tw-text-shadow-color var(--color-rose-700); /* oklch(51.4% 0.222 16.935) */ |
| text-shadow-rose-800 | --tw-text-shadow-color var(--color-rose-800); /* oklch(45.5% 0.188 13.697) */ |
| text-shadow-rose-900 | --tw-text-shadow-color var(--color-rose-900); /* oklch(41% 0.159 10.272) */ |
| text-shadow-rose-950 | --tw-text-shadow-color var(--color-rose-950); /* oklch(27.1% 0.105 12.094) */ |
| text-shadow-slate-50 | --tw-text-shadow-color var(--color-slate-50); /* oklch(98.4% 0.003 247.858) */ |
| text-shadow-slate-100 | --tw-text-shadow-color var(--color-slate-100); /* oklch(96.8% 0.007 247.896) */ |
| text-shadow-slate-200 | --tw-text-shadow-color var(--color-slate-200); /* oklch(92.9% 0.013 255.508) */ |
| text-shadow-slate-300 | --tw-text-shadow-color var(--color-slate-300); /* oklch(86.9% 0.022 252.894) */ |
| text-shadow-slate-400 | --tw-text-shadow-color var(--color-slate-400); /* oklch(70.4% 0.04 256.788) */ |
| text-shadow-slate-500 | --tw-text-shadow-color var(--color-slate-500); /* oklch(55.4% 0.046 257.417) */ |
| text-shadow-slate-600 | --tw-text-shadow-color var(--color-slate-600); /* oklch(44.6% 0.043 257.281) */ |
| text-shadow-slate-700 | --tw-text-shadow-color var(--color-slate-700); /* oklch(37.2% 0.044 257.287) */ |
| text-shadow-slate-800 | --tw-text-shadow-color var(--color-slate-800); /* oklch(27.9% 0.041 260.031) */ |
| text-shadow-slate-900 | --tw-text-shadow-color var(--color-slate-900); /* oklch(20.8% 0.042 265.755) */ |
| text-shadow-slate-950 | --tw-text-shadow-color var(--color-slate-950); /* oklch(12.9% 0.042 264.695) */ |
| text-shadow-gray-50 | --tw-text-shadow-color var(--color-gray-50); /* oklch(98.5% 0.002 247.839) */ |
| text-shadow-gray-100 | --tw-text-shadow-color var(--color-gray-100); /* oklch(96.7% 0.003 264.542) */ |
| text-shadow-gray-200 | --tw-text-shadow-color var(--color-gray-200); /* oklch(92.8% 0.006 264.531) */ |
| text-shadow-gray-300 | --tw-text-shadow-color var(--color-gray-300); /* oklch(87.2% 0.01 258.338) */ |
| text-shadow-gray-400 | --tw-text-shadow-color var(--color-gray-400); /* oklch(70.7% 0.022 261.325) */ |
| text-shadow-gray-500 | --tw-text-shadow-color var(--color-gray-500); /* oklch(55.1% 0.027 264.364) */ |
| text-shadow-gray-600 | --tw-text-shadow-color var(--color-gray-600); /* oklch(44.6% 0.03 256.802) */ |
| text-shadow-gray-700 | --tw-text-shadow-color var(--color-gray-700); /* oklch(37.3% 0.034 259.733) */ |
| text-shadow-gray-800 | --tw-text-shadow-color var(--color-gray-800); /* oklch(27.8% 0.033 256.848) */ |
| text-shadow-gray-900 | --tw-text-shadow-color var(--color-gray-900); /* oklch(21% 0.034 264.665) */ |
| text-shadow-gray-950 | --tw-text-shadow-color var(--color-gray-950); /* oklch(13% 0.028 261.692) */ |
| text-shadow-zinc-50 | --tw-text-shadow-color var(--color-zinc-50); /* oklch(98.5% 0 0) */ |
| text-shadow-zinc-100 | --tw-text-shadow-color var(--color-zinc-100); /* oklch(96.7% 0.001 286.375) */ |
| text-shadow-zinc-200 | --tw-text-shadow-color var(--color-zinc-200); /* oklch(92% 0.004 286.32) */ |
| text-shadow-zinc-300 | --tw-text-shadow-color var(--color-zinc-300); /* oklch(87.1% 0.006 286.286) */ |
| text-shadow-zinc-400 | --tw-text-shadow-color var(--color-zinc-400); /* oklch(70.5% 0.015 286.067) */ |
| text-shadow-zinc-500 | --tw-text-shadow-color var(--color-zinc-500); /* oklch(55.2% 0.016 285.938) */ |
| text-shadow-zinc-600 | --tw-text-shadow-color var(--color-zinc-600); /* oklch(44.2% 0.017 285.786) */ |
| text-shadow-zinc-700 | --tw-text-shadow-color var(--color-zinc-700); /* oklch(37% 0.013 285.805) */ |
| text-shadow-zinc-800 | --tw-text-shadow-color var(--color-zinc-800); /* oklch(27.4% 0.006 286.033) */ |
| text-shadow-zinc-900 | --tw-text-shadow-color var(--color-zinc-900); /* oklch(21% 0.006 285.885) */ |
| text-shadow-zinc-950 | --tw-text-shadow-color var(--color-zinc-950); /* oklch(14.1% 0.005 285.823) */ |
| text-shadow-neutral-50 | --tw-text-shadow-color var(--color-neutral-50); /* oklch(98.5% 0 0) */ |
| text-shadow-neutral-100 | --tw-text-shadow-color var(--color-neutral-100); /* oklch(97% 0 0) */ |
| text-shadow-neutral-200 | --tw-text-shadow-color var(--color-neutral-200); /* oklch(92.2% 0 0) */ |
| text-shadow-neutral-300 | --tw-text-shadow-color var(--color-neutral-300); /* oklch(87% 0 0) */ |
| text-shadow-neutral-400 | --tw-text-shadow-color var(--color-neutral-400); /* oklch(70.8% 0 0) */ |
| text-shadow-neutral-500 | --tw-text-shadow-color var(--color-neutral-500); /* oklch(55.6% 0 0) */ |
| text-shadow-neutral-600 | --tw-text-shadow-color var(--color-neutral-600); /* oklch(43.9% 0 0) */ |
| text-shadow-neutral-700 | --tw-text-shadow-color var(--color-neutral-700); /* oklch(37.1% 0 0) */ |
| text-shadow-neutral-800 | --tw-text-shadow-color var(--color-neutral-800); /* oklch(26.9% 0 0) */ |
| text-shadow-neutral-900 | --tw-text-shadow-color var(--color-neutral-900); /* oklch(20.5% 0 0) */ |
| text-shadow-neutral-950 | --tw-text-shadow-color var(--color-neutral-950); /* oklch(14.5% 0 0) */ |
| text-shadow-stone-50 | --tw-text-shadow-color var(--color-stone-50); /* oklch(98.5% 0.001 106.423) */ |
| text-shadow-stone-100 | --tw-text-shadow-color var(--color-stone-100); /* oklch(97% 0.001 106.424) */ |
| text-shadow-stone-200 | --tw-text-shadow-color var(--color-stone-200); /* oklch(92.3% 0.003 48.717) */ |
| text-shadow-stone-300 | --tw-text-shadow-color var(--color-stone-300); /* oklch(86.9% 0.005 56.366) */ |
| text-shadow-stone-400 | --tw-text-shadow-color var(--color-stone-400); /* oklch(70.9% 0.01 56.259) */ |
| text-shadow-stone-500 | --tw-text-shadow-color var(--color-stone-500); /* oklch(55.3% 0.013 58.071) */ |
| text-shadow-stone-600 | --tw-text-shadow-color var(--color-stone-600); /* oklch(44.4% 0.011 73.639) */ |
| text-shadow-stone-700 | --tw-text-shadow-color var(--color-stone-700); /* oklch(37.4% 0.01 67.558) */ |
| text-shadow-stone-800 | --tw-text-shadow-color var(--color-stone-800); /* oklch(26.8% 0.007 34.298) */ |
| text-shadow-stone-900 | --tw-text-shadow-color var(--color-stone-900); /* oklch(21.6% 0.006 56.043) */ |
| text-shadow-stone-950 | --tw-text-shadow-color var(--color-stone-950); /* oklch(14.7% 0.004 49.25) */ |

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

