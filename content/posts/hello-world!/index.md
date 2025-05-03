---
title: "Hello, world! ;)"
date: 2025-02-19T17:00:00-00:00
summary: "The reverse Flynn Effect and building a static website"
thumbnail_image: OsakaSkyline.jpeg
thumbnail_caption: "A picture I took of the skyline in Osaka, Japan in the Summer of '24"
draft: false
---

<!-- {{< quotation >}}
What lies behind us and what lies ahead of us are tiny matters compared to what lies within us.
--- *Meditations in Wall Street*, though it is oft attributed to Ralph Waldo Emerson.
{{</ quotation >}} -->

I've attempted a blog on and off ever since my computer science teacher suggested that I should start one back in 7th grade. While none of these attempts have proven fruitful in the long run, the culmination of several factors --- including the rapid arrival of a new year, the relative freedom of second semester senior year, and the rapidly approaching onset of adulthood --- have inspired me to try my hand at it one last time. Underlying it all is the development of a newfound interest in writing and rhetoric recently brought about by reading a series of interesting books, in addition to some rather foundational documents and (perhaps most appropriately) some interesting blog posts scattered throughout the internet. I used to dismiss writing in favor of a more STEM-focused pursuit of technology and engineering, but I've now come to realize the power of the written and spoken word. Assembly may have landed the Apollo spacecraft, but it was Kennedy's speech that inspired men to do so great a thing[^1]. 

Still, writing is far more than a purely rhetorical tool; it's as a method for articulating complex thoughts and 
presenting them in a comprehensible way in a manner that, ironically, reminds a little of the act of writing clever 
programs. Of course, it's all the more powerful if such arguments are written with persuasion and flow, but that belabors 
the fundamental point of this undertaking. I think this pursuit has taken a special sort of importance to me in this 
modern age, where endless distraction from short-form video, addictive social media algorithms, online shopping, TV shows, video games --- the worst of which being a thinly veiled Skinner box --- and everything in-between (seriously, take your pick!) further shortens our already strained attention spans and capacity for distress tolerance. With our smartphones always at
arm's reach (and smartwatches even closer), how could we possibly bear to be bored, or even delay gratification 
long enough to read a good book cover to cover?

Many will agree with this sentiment intrinsically, but I believe society's intellectual decline is clearly evident in several quantitative trends as well. In the past, each successive generation was progressively smarter than the last, as evidenced by a steady rise in IQ test scores over a period of several decades in a phenomenon discovered by researcher James Flynn and thus dubbed the "Flynn Effect." Recently, however, that trend has reversed writ large: Americans, particularly those aged 18-24, have . This finding is also consistent with results from other countries, including Norway, Finland, and France.

https://www.sciencedirect.com/science/article/pii/S0160289623000156
https://www.dailymail.co.uk/health/article-11841169/IQ-scores-dropped-time-nearly-100-years.html

This find


Test scores certainly aren't the be-all and end-all of measuring intelligence. But other activities that we might consider measures of an
educated society, like reading books, are also seeing recent declines.

Anecdotal evidence on this phenomenon is not difficult to find either. 

...
I find myself clutching tightly to the belief that writing something --- *anything* at all -- is better than engaging with the latest AI generated slop.

The evidence suggests we've passed peak intelligence.


What's the solution to our intellectual woes? I can't pretend to know, but I'm tempted to take my high school English teacher's advice to, above all else, "just write." 

Writing, or even reading for that matter, almost feels like an act of resistance --- a concentrated effort to engage with a topic for an extended period of time in a manner that offers a kind of intellectual stimulation that our modern conveniences don't. I think David Brooks put it best in his essay ["Producing Something This Stupid Is the Achievement of a Lifetime."](https://www.nytimes.com/2025/04/10/opinion/education-smart-thinking-reading-tariffs.html?smid=nytcore-android-share)[^2]


> Reading a book puts you inside another person’s mind in a way that a Facebook post just doesn’t. Writing is the 
discipline that teaches you to take a jumble of thoughts and cohere them into a compelling point of view...Once you start 
using your mind, you find that learning isn’t merely calisthenics for your ability to render judgment; it’s intrinsically fun.

<!-- It is with that spirit in mind that I begin this blog. -->

With that said, I won't make any promises about this blog's future content; frankly, I don't even know. My last attempts almost entirely focused on my technical endeavors, and I'll surely continue that trend in many a blog to come, but I'm tempted to explore a wider ranger topics pertaining to my multifaceted interests this time around. Perhaps my intentions are, on a fundamental level, *selfish* --- part of a Maslowian desire to self-actualize or to prove that I, for a fleeting moment, was really *here*, with everything I've done and all the insights I've discovered. At the very least, I might train my mind and become more focused and articulate in the process. 

I wouldn't be surprised if many of these posts amount to essentially long-form elaborations on the notes I've written to myself, scrawled in slips of eco-friendly paper torn from a cheap pocket notebook and shoved in a Manila folder I keep in my cupboard, or hastily typed into my Notes app and the `.txt` files sprinkled throughout my file system. Clearly, they were important to me at the time.

And who knows? Maybe someone, *somewhere* will derive some value from this little venture of mine. If even a single interesting half-thought transpires from these writings, that would be enough.

## Website Details
I find it be only natural, for my first post, to entertain a brief explanation of how I built this blog in the first place. For maximum control, I've decided to build my own website from scratch instead of rolling out a WordPress instance or similar prepacked alternative. The biggest component of the so-called 'stack' is Hugo, which is used to generate a static website that is then hosted (for *free!*) on GitHub pages[^3].

Static keeps it simple. Static keeps it fast. But, most importantly, static keeps it cheap. In fact, the only cost associated with running my little place on the great World Wide Web is the domain, which I pay Namecheap ~~$11.28~~ $16.68 a year for.

![My Namecheap Dashboard](DomainListNamecheap.png)

In terms of static site generators, I found Hugo felt lighter and faster that Jeykll, while remaining more verstaile and documented then Eleventy (at least at the last time I used it). I don't use a theme, so the task of making things look 'good' is handled by Tailwind CSS through in-line classes in the different Hugo layouts, as shown in this code snippet from the single page layout (i.e. the layout for this very post):
```
{{ define "main" }}
<div class="bg-white dark:bg-zinc-800 mx-3 sm:mx-[5%] md:mx-[10%] lg:mx-[15%] my-9">
  <h1 class="text-4xl font-bold tracking-tight text-gray-900 dark:text-gray-100 sm:text-6xl mb-3">{{ .Title }}</h1>
  <p class="text-base tracking-tight text-gray-600 dark:text-gray-300 sm:text-2xl mb-3">{{ .Params.summary }}</p>
  <img width="100%" src="{{ .Params.thumbnail_image }}"></img>
  <p class="text-sm font-serif text-gray-600 dark:text-gray-300 sm:text-base mt-3 mb-5">{{ .Params.thumbnail_caption }}</p>
  <div class="text-lg text-justify leading-8 text-gray-600 dark:text-gray-300 content">{{ .Content }}</div>
</div>
{{ end }}
```

These pre-existing utility classes make styling much easier out of the box in comparison to writing custom CSS. The end 
result is also more consistent, because I'm using the same utility classes and styles everywhere. Moreover, Tailwind's inline classes make it rather trivial to make the website responsive and add a dark mode. Responsiveness is baked right in using sensible breakpoint prefixes like `sm:`, `md:`, `lg:`, which trigger the specific labeled styles after the window goes past a certain minimum width. Meanwhile, Tailwind uses the `dark:` prefix to define styles that only activate when dark mode is enabled, which is done in this specific website by adding the `dark` class to the body of the page.

On the other hand, the actual functionality of the dark mode button --- represented as a sun and moon icon in the navigation bar --- is handled with a bit of client-side Javascript:
```
// Index.JS

// Dark mode
var darkMode;

if (localStorage.theme === "dark" || !("theme" in localStorage)) {
  document.getElementById("moon").classList.add("hidden");
  document.getElementById("sun").classList.remove("hidden");

  document.getElementById("light-theme").setAttribute("disabled", "disabled");

  document.documentElement.classList.add("dark");
  darkMode = true;
} else {
  document.getElementById("moon").classList.remove("hidden");
  document.getElementById("sun").classList.add("hidden");

  document.getElementById("dark-theme").setAttribute("disabled", "disabled");
  
  document.documentElement.classList.remove("dark");
  darkMode = false;
};

function toggleDarkMode() {
  if (darkMode) {
    document.getElementById("moon").classList.remove("hidden");
    document.getElementById("sun").classList.add("hidden");

    document.getElementById("light-theme").removeAttribute("disabled");
    document.getElementById("dark-theme").setAttribute("disabled", "disabled");

    darkMode = false;
    document.documentElement.classList.remove("dark");
    localStorage.theme = "light";
  }

  else if (!darkMode) {
    document.getElementById("moon").classList.add("hidden");
    document.getElementById("sun").classList.remove("hidden");

    document.getElementById("light-theme").setAttribute("disabled", "disabled");
    document.getElementById("dark-theme").removeAttribute("disabled");

    darkMode = true;
    document.documentElement.classList.add("dark");
    localStorage.theme = "dark";
  }
}

document.getElementById("theme-switcher").addEventListener("click", toggleDarkMode);
```

Since, I use a static sight generator, I just write the posts in Markdown and Hugo automatically generates the corresponding HTML, allowing me to have a decent [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns) between content, website structure, and styling. In accordance with this philosophy, I 
keep my c

Markdown also has an advantage of keeping my blog posts 

While writing blog posts in plain-text --- or at least a very-lightweight markup language --- is convenient, I lose control of the ability to style my content directly as the generated HTML lacks Tailwind's inline classes. This is especially problematic because Tailwind strips away the default margins of most elements, leading to situations where all the text in a post clumps together in one big paragraph because
there is virtually no spacing between elements. I initially turned to Hugo feature called `shortcodes`, since Hugo --- unlike most other programs that use Markdown files --- does not support HTML in Markdown files by default (though I did eventually enable this behavior).

 does raise an some issues since I'm unable  as it means that I'm unable to style 
To further aid with the responsiveness of it all, I use the aforementioned Tailwind inline classes to hide the full navigation bar and showcase a collapseable 'hamburger' menu in its place on mobile devices.

```
<!-- navbar.HTML -->
<div class="block sm:hidden">
  <button id="navbar-toggle" class="flex items-center px-3 py-2 border rounded text-gray-500 dark:text-gray-200 border-gray-300 dark:border-gray-500 hover:text-black hover:border-black">
    <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Menu</title><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
  </button>
</div>
<div id="menu-list" class="w-full block flex-grow sm:flex sm:items-center sm:w-auto hidden">
  <div class="text-sm sm:flex-grow">
    {{ range .Site.Menus.nav }}
      <a href="{{ .URL }}" class="block mt-4 sm:inline-block sm:mt-0 text-gray-500 dark:text-gray-300 hover:text-black dark:hover:text-white mr-4">
        {{ .Name }}
      </a>
    {{ end }}
  </div>
</div>
```


This requires a few lines of Javascript to show the menu list when the hamburger menu is clicked on, as shown by this code 
highlight:
```
// Navbar
var collapsed = true;

function toggleNavbar() {
  if (collapsed) {
    document.getElementById("menu-list").classList.remove("hidden");
    document.getElementById("theme-button").classList.remove("hidden");

    collapsed = false;
  }

  else if (!collapsed) {
    document.getElementById("menu-list").classList.add("hidden");
    document.getElementById("theme-button").classList.add("hidden");

    collapsed = true;
  }
}

document.getElementById("navbar-toggle").addEventListener("click", toggleNavbar);
```

Speaking of code highlighting, I use highlight.js with the 
The only JavaScript that is really needed is for managing the menu, dark mode, and code highlights

continuous integration to build hugo with github

also markdown makes it easier to switch platforms later


[^1]: Well... that and the Cold War...
[^2]: He also makes a similar point on the intellectual regression of society, as reflected in Trump's tarrif policy. Hence the title, "Producing Something This Stupid Is the Achievement of a Lifetime."
[^3]: I do plan to set up a Cisco UCS C220 M3 rack server I've recently acquired, opening the door to hosting things like a mail or Git server on this domain in the near future. Still, the cost would still be nothing more than the electricity required to run the thing --- and the noise pollution in my room, because that thing is *loud*.
