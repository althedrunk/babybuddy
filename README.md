<img src="babybuddy/static_src/logo/icon.png" height="150" align="left">

# Baby Buddy (Imperial / lbs & oz Fork)

[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Gitter](https://img.shields.io/gitter/room/nwjs/nw.js.svg)](https://gitter.im/babybuddy/Lobby)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

> **This is a fork of [babybuddy/babybuddy](https://github.com/babybuddy/babybuddy) with modifications to default weight tracking to pounds and ounces (lbs/oz) instead of kilograms.**
> See [Changes from upstream](#-changes-from-upstream) below for full details.

A buddy for babies! Helps caregivers track sleep, feedings, diaper changes,
tummy time and more to learn about and predict baby's needs without (_as much_)
guess work.

![Baby Buddy desktop view](screenshot.png)

![Baby Buddy mobile views](screenshot_mobile.png)

## 🔧 Changes from upstream

This fork modifies the official Baby Buddy project in the following ways:

### Weight tracking in lbs & oz

- **Default weight unit is pounds and ounces (lbs/oz)** for all new users. Kilograms remain available as a per-user setting under *User Settings → Weight Unit*.
- **Weight entry uses two separate fields** — *Pounds* and *Ounces* — so you never need to do decimal conversions. Just type `13` lbs and `7` oz.
- **Weight is stored as total ounces** internally (e.g. 13 lbs 7 oz = 215 oz), which avoids floating-point rounding issues with values like 10–15 oz.
- **Weight lists and graphs** display values in the format `X lbs Y oz` when lbs/oz is selected.

> **Migrating from the official image?** If your existing weight entries were recorded in the legacy `lbs.oz` decimal format (e.g. `13.7` to mean 13 lbs 7 oz), the included database migration (`core/0036`) will automatically convert them to the new total-ounces format on first run.

### Docker / self-hosting

A `Dockerfile` and `babybuddy/settings/docker.py` are included so you can build and run this fork directly from source without relying on the upstream Docker Hub image.

Quick start with Docker Compose — replace the official image reference:

```yaml
services:
  babybuddy:
    build:
      context: /path/to/this/repo
      dockerfile: Dockerfile
    image: babybuddy-local:latest
    environment:
      - DJANGO_SETTINGS_MODULE=babybuddy.settings.docker
      - SECRET_KEY=your-secret-key-here
      - DB_ENGINE=django.db.backends.postgresql
      - DB_NAME=babybuddy
      - DB_USER=youruser
      - DB_PASSWORD=yourpassword
      - DB_HOST=babybuddy-db
      - DB_PORT=5432
      - CSRF_TRUSTED_ORIGINS=https://yourdomain.com
    volumes:
      - ./media:/app/media
    ports:
      - "8000:8000"
```

Migrations (including the weight conversion) run automatically on container startup.

---

## 👾 Demo

A [demo of Baby Buddy](https://demo.baby-buddy.net) is available. The demo instance
resets every hour. Login credentials are:

- Username: `admin`
- Password: `admin`

## 📘 Documentation

Visit [https://docs.baby-buddy.net](https://docs.baby-buddy.net) for full documentation.

### Additional documentation

- [Security](/SECURITY.md)
- [License](/LICENSE) (BSD-2 Clause)

## 🗺️ Languages

Baby Buddy is available in a variety of languages thanks to the efforts of numerous
translators. Language can be set on a per-user basis from the user settings page
(`/user/settings/`). See [Contributing](https://docs.baby-buddy.net/contributing/translation/)
for information about how to create/update translations.

### Available languages

:brazil: Brazilian Portuguese, :es: Catalan, :cn: Chinese (simplified), :croatia: Croatian, :czech_republic: Czech, :denmark: Danish, :netherlands: Dutch, :uk: English (U.K.), :us: English (U.S.) (base), :finland: Finnish, :fr: French, :de: German, :israel: Hebrew, :hungary: Hungarian, :it: Italian, :jp: Japanese, :norway: Norwegian Bokmål, :poland: Polish, :portugal: Portuguese, :ru: Russian, :serbia: Serbian, :mexico: :es: Spanish, :sweden: Swedish, :tr: Turkish, :ukraine: Ukrainian

## 🌐 Baby Buddy on the Web

This is a non-exhaustive list of neat projects and blog posts that either extend
or use Baby Buddy in fun ways. If you have a project to share please open a PR
adding it here or reach out via GitHub Issues or Discussions or on Gitter!

### Smart home

- [Home Assistant Addon](https://github.com/OttPeterR/addon-babybuddy) (host Baby Buddy on Home Assistant)
- [Home Assistant integration](https://github.com/jcgoette/baby_buddy_homeassistant) (monitor and use Baby Buddy from Home Assistant)
- [How to Setup Baby Buddy in Home Assistant](https://smarthomescene.com/guides/how-to-setup-baby-buddy-in-home-assistant/)
- [Baby Buddy and Home Assistant](https://martinnoah.com/babybuddy-and-home-assistant.html)
- [Alexa skill](https://github.com/babybuddy/babybuddy-alexa-skill)

### Hardware

- [Bottle Scale for BabyBuddy and Home Assistant with ESPHome](https://github.com/sfgabe/OITProjects/tree/master/BabyBuddy_ESP_HASS)
- [Quick Entry Keypad (ESP8266)](https://github.com/sfgabe/OITProjects/tree/master/Baby_Buddy_Keypad)
- [Baby Buddy Keypad (ESP32)](https://github.com/jeroenterheerdt/Baby-Buddy-Keypad)
- [BabyScout](https://github.com/MikeSchapp/BabyScout) - Keypad for recording diaper changes, feedings and sleep to BabyBuddy
- [BabyPod](https://www.printables.com/model/872095-babypod-a-remote-control-for-baby-buddy-for-new-pa) - A remote control for Baby Buddy for new parents (sources: [hardware](https://github.com/skjdghsdjgsdj/babypod-hardware), [software](https://github.com/skjdghsdjgsdj/babypod-software/))
- [MatrixPortal BabyBuddy](https://github.com/skjdghsdjgsdj/matrixportal-babybuddy)

### Mobile

- [Baby Buddy for Android](https://play.google.com/store/apps/details?id=eu.pkgsoftware.babybuddywidgets) ([Source](https://github.com/babybuddy/babybuddy-for-android))
- [iOS shortcuts](https://github.com/babybuddy/babybuddy/discussions/300)
- [Convert exported data from "Baby tracker - feeding, sleep and diaper" mobile app to Baby Buddy](https://github.com/babybuddy/babybuddy/discussions/424)

### Videos

- [Baby Buddy: Keep Records of Your Child/Baby's Growth and Activities](https://www.youtube.com/watch?v=sO6rjn2s6-k)

### Other

- [Grafana Dashboard](https://github.com/babybuddy/babybuddy/discussions/607)
- [Sandstorm app](https://github.com/babybuddy/babybuddy-sandstorm)
- Newborn parenting software series (API, buttons, LCD information screen!)
  - [part 1](https://lutzky.net/2021/10/03/software-parenting-1/)
  - [part 2](https://lutzky.net/2021/10/05/software-parenting-2/)
  - [part 3](https://lutzky.net/2021/10/10/software-parenting-3/)
- [High Level Developer Documentation (AI-Generated)](https://wiki.mutable.ai/babybuddy/babybuddy)
- [Example custom TypeScript frontend](https://github.com/jkjustjoshing/maddie-buddy) (based on [Remix](https://remix.run/))

## 🔐 Reporting Vulnerabilities

See [SECURITY.md](SECURITY.md) for information about where and how to report
potential Baby Buddy vulnerabilities.

## ❤️ Support

### Contribution and sponsorship

Contribute or sponsor Baby Buddy's contributors using any of the following methods:

- [Sponsor @babybuddy on GitHub](https://github.com/sponsors/babybuddy)
- [Sponsor @cdubz on GitHub](https://github.com/sponsors/cdubz)
- [Contribute on Open Collective](https://opencollective.com/babybuddy)

### Tools and infrastructure

The following organizations and services support Baby Buddy contributors in various ways (software licensing, service credits, etc.).

_Some of the links below use referral codes -- all referral proceeds are treated as contributions to the Baby Buddy project._

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%203.svg)](https://www.digitalocean.com/?refcode=dd79e4cfd7b6&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)
[<img src="https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png" width="100" alt="JetBrains Logo (Main) logo.">](https://www.jetbrains.com/community/opensource/)
[![POEditor](https://poeditor.com/public/images/ui/logos/logo_dark.svg)](https://poeditor.com/)
