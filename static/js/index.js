var darkMode;

if (localStorage.theme === 'dark' || !('theme' in localStorage)) {
    document.getElementById("moon").classList.add("hidden");
    document.getElementById("sun").classList.remove("hidden");

    document.documentElement.classList.add('dark');
    darkMode = true;
  } else {
    document.getElementById("moon").classList.remove("hidden");
    document.getElementById("sun").classList.add("hidden");
    
    document.documentElement.classList.remove('dark');
    darkMode = false;
};

function toggleDarkMode() {
  if (darkMode) {
    document.getElementById("moon").classList.remove("hidden");
    document.getElementById("sun").classList.add("hidden");

    darkMode = false;
    document.documentElement.classList.remove("dark");
    localStorage.theme = "light";
  }

  else if (!darkMode) {
    document.getElementById("moon").classList.add("hidden");
    document.getElementById("sun").classList.remove("hidden");

    darkMode = true;
    document.documentElement.classList.add("dark");
    localStorage.theme = "dark";
  }
}

document.getElementById("theme-switcher").addEventListener("click", toggleDarkMode);