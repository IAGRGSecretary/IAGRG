---
layout: default
title: Resources for Researchers
---

<link rel="stylesheet" href="{{ '/assets/css/style-resources.css' | relative_url }}">

<header class="resources-header">
  <div class="container">
    <h1>Research Resources</h1>
    <p>
A curated collection of research tools, learning resources, and leading
institutions in general relativity and gravitation.
</p>
  </div>
</header>

<section class="resources-page container">

  <section class="knowledge-hero-image">

    <figure class="hub-figure">
      <img
        src="{{ '/assets/img/mega-science_banner_smaller.webp' | relative_url }}"
        alt="From micro to macro: understanding the universe through mega science projects"
      >

      <figcaption>
        Visual courtesy of <strong>Vigyan Samagam</strong>
      </figcaption>
    </figure>

  </section>

<section class="resource-container global-centers">

  <div class="resource-section-header narrow">
    <h2 class="category-title">Global Research Centers</h2>
    <p class="section-intro">
      A curated directory of leading institutions and research groups in general relativity and gravitation across the world.
    </p>
  </div>

  <div class="accordion-wrapper wide">

    {% for region in site.data.global_resources %}

    <details class="region-block" {% if forloop.first %}open{% endif %}>
      <summary class="region-summary">{{ region.region }}</summary>

      <div class="institution-grid">
        {% for inst in region.institutions %}
        <a href="{{ inst.url }}" target="_blank" class="inst-card">
          <span class="inst-name">{{ inst.name }}</span>
          <span class="inst-url">{{ inst.display }}</span>
        </a>
        {% endfor %}
      </div>

    </details>

    {% endfor %}

  </div>

</section>
