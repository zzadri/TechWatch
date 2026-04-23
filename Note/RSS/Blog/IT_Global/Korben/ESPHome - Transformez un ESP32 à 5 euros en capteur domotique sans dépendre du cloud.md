---
title: "ESPHome - Transformez un ESP32 à 5 euros en capteur domotique sans dépendre du cloud"
author: "Korben"
date: 2026-02-19T09:15:34.000Z
type: site
subject:
category: IT Global
tags:
  - "hardware-diy/arduino-electronique"
  - "linux-open-source/self-hosting"
  - "tutoriels-guides/tutoriels-avances"
  - "capteur temperature"
  - "DIY"
  - "domotique"
  - "ESP32"
  - "ESPHome"
  - "Home Assistant"
  - "IoT local"
rss_source: Blog
url: https://korben.info/esphome-esp32-capteur-temperature-home-assistant.html
note: 0
seen: false
---

<p>Aujourd'hui j'aimerais vous parler un peu de bidouille et plus particulièrement de domotique. Hé oui, si comme moi, vous en avez marre que tous vos objets connectés passent par des serveurs chinois (souvent à la sécurité douteuse) ou américains (souvent directement connecté à la NSA) pour vous dire qu'il fait 22°C dans votre salon, on va voir comment ensemble créer ses propres capteurs 100% locaux avec <strong>
<a href="https://esphome.io/">ESPHome</a>
</strong>.</p>
<p>ESPHome, c'est un framework open source qui transforme n'importe quel ESP32 ou ESP8266 en appareil connecté intelligent sans vous prendre la tête. Vous écrivez un petit fichier YAML, vous flashez la puce, et hop, vous avez un capteur qui cause directement avec Home Assistant. Comme ça y'a pas de cloud et encore moins de données qui partent on ne sait où.</p>
<p>Et c'est hyper accessible... Suffit de savoir remplir un fichier texte avec quelques indentations (le fameux YAML), et voilà vous savez utiliser ESPHome.</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/esphome-esp32-capteur-temperature-home-assistant/esphome-esp32-capteur-temperature-home-assistant-2.png" alt="" loading="lazy" decoding="async">
<p><em>ESPHome fait partie de l'Open Home Foundation (
<a href="https://esphome.io/">Source</a>
)</em></p>
<h3 id="ce-quil-vous-faut">Ce qu'il vous faut</h3>
<ul>
<li>Un ESP32 (genre un Wemos D1 Mini ou un NodeMCU)</li>
<li>Un capteur DHT22 (température et humidité)</li>
<li>Quelques fils Dupont</li>
<li>Temps estimé : 30 minutes</li>
</ul>
<p>Niveau branchement, c'est pas sorcier. Le DHT22 a 3 broches utiles : VCC sur le 3.3V de l'ESP, GND sur GND, et DATA sur un GPIO de votre choix (le GPIO4 marche nickel). Pensez aussi à ajouter une résistance de 4.7kΩ entre DATA et VCC si vous voulez des lectures béton (beaucoup de modules l'ont déjà intégrée, mais vérifiez bien).</p>
<img src="https://korben.info/cdn-cgi/image/width=1200,fit=scale-down,quality=90,f=avif/esphome-esp32-capteur-temperature-home-assistant/esphome-esp32-capteur-temperature-home-assistant-1.webp" alt="" loading="lazy" decoding="async">
<p><em>
<a href="https://randomnerdtutorials.com/esp32-dht11-dht22-temperature-humidity-sensor-arduino-ide/">source</a>
</em></p>
<p>Ensuite, pour installer ESPHome sur votre ordi, ça se passe avec pip :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">pip install esphome
</span></span></code></pre><p>Une fois l'outil en place, vous créez votre configuration YAML. Voici un exemple tout simple pour notre capteur :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">esphome:
</span></span><span class="line"><span class="cl"> name: capteur_salon
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">esp32:
</span></span><span class="line"><span class="cl"> board: esp32dev
</span></span><span class="line"><span class="cl">
</span></span><span class="line"><span class="cl">sensor:
</span></span><span class="line"><span class="cl"> - platform: dht
</span></span><span class="line"><span class="cl"> pin: GPIO4
</span></span><span class="line"><span class="cl"> temperature:
</span></span><span class="line"><span class="cl"> name: &#34;Température Salon&#34;
</span></span><span class="line"><span class="cl"> humidity:
</span></span><span class="line"><span class="cl"> name: &#34;Humidité Salon&#34;
</span></span><span class="line"><span class="cl"> update_interval: 60s
</span></span></code></pre><p>Hé voilà ! Ce fichier suffit à tout configurer. Ensuite, pour flasher, branchez votre ESP en USB et lancez la commande :</p>
<div class="highlight"><pre tabindex="0" class="chroma"><code class="language-fallback" data-lang="fallback"><span class="line"><span class="cl">esphome run capteur_salon.yaml
</span></span></code></pre><p>La première fois, ça compile tout le firmware et ça flashe. Une fois que c'est fait, l'ESP apparaît automatiquement dans Home Assistant si vous avez activé l'intégration. Et le top du top, c'est que les prochaines mises à jour se feront en WiFi (OTA), ce qui est super pratique quand le truc est planqué derrière un meuble.</p>
<p>Et si vous voulez aller plus loin dans l'intégration domotique locale, je vous conseille aussi de voir comment
<a href="https://korben.info/comment-faire-fonctionner-un-module-razberry-2-gpio-avec-home-assistant.html">utiliser le GPIO directement sur Home Assistant</a>
.</p>
<p>Et voilà comment, avec dix balles et un peu de curiosité, vous avez un capteur qui n'espionne plus votre vie. Youuhouuu !</p>