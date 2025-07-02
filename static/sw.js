self.addEventListener("install", (e) => {
  e.waitUntil(
    caches.open("pwa-cache").then((cache) =>
      cache.addAll(["/", "/static/css/styles.css", "/static/manifest.json"])
    )
  );
});

self.addEventListener("fetch", (e) => {
  e.respondWith(
    caches.match(e.request).then((res) => res || fetch(e.request))
  );
});
