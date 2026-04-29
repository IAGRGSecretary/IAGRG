---
layout: default
title: Vaidya–Raychaudhuri Endowment Lecture Awards
---

<link rel="stylesheet" href="{{ '/assets/css/style-awards.css' | relative_url }}">

<header class="award-hero">
  <div class="container">
    <p class="award-kicker">IAGRG Awards</p>

    <h1>Vaidya–Raychaudhuri Endowment Lecture Awards</h1>

    <p class="award-subtitle">
      Recognising excellence in research and teaching of General Relativity and its applications
    </p>

  </div>
</header>

<!-- ABOUT SECTION -->
<section class="archive-container">

  <details class="about-block" open>
    <summary class="about-summary">About this Lecture Series</summary>

    <div class="about-content">

      <p>
        Instituted as a tribute to two doyens of Indian relativity research,
        <a href = "{{'https://en.wikipedia.org/wiki/Prahalad_Chunnilal_Vaidya'|relative_url}}" target = "_blank"><strong>P. C. Vaidya</strong></a> and <a href = "{{'https://en.wikipedia.org/wiki/Amal_Kumar_Raychaudhuri'|relative_url}}" target ="_blank"><strong>A. K. Raychaudhuri </strong></a>, this distinguished lecture recognises exceptional contributions in both research and teaching of General Relativity and its applications to astrophysics and cosmology. The awardee is invited to deliver the <strong>Vaidya–Raychaudhuri Lecture</strong>, traditionally designed to be accessible to the wider gravitation community.
      </p>
      <p>
        The first lecture was delivered at the <strong>15th IAGRG Meeting in 1989</strong>, and it has remained an integral part of IAGRG activities ever since. Since the <strong>26th IAGRG Meeting in 2011</strong>, the lecture has been held annually: during IAGRG meetings in alternate years, and between meetings at venues decided by the General Body Meeting.
      </p>
    </div>

  </details>

</section>

<!-- ARCHIVE SECTION -->
<section class="archive-container">

  <div class="archive-card">

    <div class="archive-header">
      <h2>Lecture Archive</h2>
    </div>

    <div class="vr-archive">

      {% for period in site.data.vr_lectures %}

      <details {% if forloop.first %}open{% endif %}>
        <summary>{{ period.decade }}</summary>

        <div class="vr-details-content">

          <div class="vr-grid">

            {% for lecture in period.lectures %}

            <article class="vr-card">

              <div class="vr-number">#{{ lecture.number }}</div>

              <h3>{{ lecture.speaker }}</h3>

              <p class="vr-meta">
                <strong>Year:</strong> {{ lecture.date }}<br>
                <strong>Venue:</strong> {{ lecture.venue }}
              </p>

              <p class="vr-title">
                {{ lecture.title }}
              </p>

              {% if lecture.link %}
              <a href="{{ lecture.link }}" class="vr-link">Read More →</a>
              {% endif %}

            </article>

            {% endfor %}

          </div>

        </div>
      </details>

      {% endfor %}

    </div>

  </div>

</section>
