---
layout: default
title: IAGRG Workshops & Schools
---

<link rel="stylesheet" href="{{ '/assets/css/style-meetings.css' | relative_url }}">

<header class="page-header">
  <div class="container">
    <h1>IAGRG Schools & Workshops</h1>
    <p>
      Specialized workshops and schools organized or supported by IAGRG.
    </p>
  </div>
</header>

<main class="container">

<details class="about-block">
<summary class="about-summary">About IAGRG Schools/Workshops</summary>

<div class="about-content">
IAGRG also organizes and sponsors workshops and schools from time to time. These are usually more specialized in nature, with themes that evolve according to current developments in gravitation, cosmology and related areas.
</div>

</details>

<div class="archive-container">

<!-- ===================== -->
<!-- IAGRG SCHOOLS -->
<!-- ===================== -->

<h2 class="section-title">IAGRG Schools</h2>

{% for period in site.data.iagrg_schools %}

{% assign schools = period.meetings | where: "type", "school" %}

{% if schools.size > 0 %}

<details class="decade-block" {% if forloop.first %}open{% endif %}>
<summary class="decade-summary">{{ period.decade }}</summary>

<div class="details-content">
<div class="meeting-grid">

{% for meeting in schools %}

<div class="meeting-card">

<div class="meeting-header">
<div>

<h3 class="meeting-title">
  {% if meeting.link %}
    <a href="{{ meeting.link |relative_url}}" target="_blank" rel="noopener">
      {{ meeting.title }}
    </a>
  {% else %}
    {{ meeting.title }}
  {% endif %}
</h3>

<div class="meeting-date">{{ meeting.date }}</div>
</div>

<div class="meeting-badge">#{{ meeting.number }}</div>
</div>

<div class="meeting-meta">
<strong>Venue:</strong> {{ meeting.venue }}
</div>

</div>

{% endfor %}

</div>
</div>
</details>

{% endif %}
{% endfor %}



<!-- ===================== -->
<!-- IAGRG WORKSHOPS -->
<!-- ===================== -->

<h2 class="section-title">IAGRG Workshops</h2>

{% for period in site.data.iagrg_schools %}

{% assign workshops = period.meetings | where: "type", "workshop" %}

{% if workshops.size > 0 %}

<details class="decade-block">
<summary class="decade-summary">{{ period.decade }}</summary>

<div class="details-content">
<div class="meeting-grid">

{% for meeting in workshops %}

<div class="meeting-card">

<div class="meeting-header">
<div>
<h3 class="meeting-title">{{ meeting.title }}</h3>
<div class="meeting-date">{{ meeting.date }}</div>
</div>

<div class="meeting-badge">#{{ meeting.number }}</div>
</div>

<div class="meeting-meta">
<strong>Venue:</strong> {{ meeting.venue }}
</div>

</div>

{% endfor %}

</div>
</div>
</details>

{% endif %}
{% endfor %}

</div>
</main>
