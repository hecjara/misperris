var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/estilos.css',
    '/static/core/img/rescate.jpg',
    '/static/core/img/logo.png',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/correo.png',
    '/static/core/img/social-inst.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/socialplus.png',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css'

];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            

            return fetch(event.request).catch(function(){
                return response;
            });
        })
    );
});