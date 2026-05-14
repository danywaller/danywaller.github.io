---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of the public pages and collections currently enabled on the site. For robots, there is also an [XML sitemap]({{ base_path }}/sitemap.xml).

{% assign public_pages = site.pages | where_exp: "item", "item.sitemap != false and item.title and item.url != '/sitemap/'" | sort: "url" %}
{% assign public_collections = site.collections | where_exp: "collection", "collection.output != false and collection.label != 'posts'" %}

<h2>Pages</h2>
{% for post in public_pages %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in public_collections %}
  {% assign public_docs = collection.docs | where_exp: "doc", "doc.sitemap != false" %}
  {% if public_docs.size > 0 %}
    {% capture label %}{{ collection.label }}{% endcapture %}
    {% if label != written_label %}
  <h2>{{ label }}</h2>
      {% capture written_label %}{{ label }}{% endcapture %}
    {% endif %}
    {% for post in public_docs %}
  {% include archive-single.html %}
    {% endfor %}
  {% endif %}
{% endfor %}
