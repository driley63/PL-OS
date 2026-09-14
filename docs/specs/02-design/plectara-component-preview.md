# Plectara component color preview

Use the theme switch in the header to review light and dark modes. These samples use the exported color roles; the component library's spacing, radii, type scale, and interaction standards remain unchanged. The field is a local visual sample and does not save data.

<div class="plectara-preview" markdown="1">

## A small step, a clearer picture

<p class="secondary">Supporting text uses a theme-specific slate tone.</p>
<label for="brand-sample">Sample capture note</label>
<input id="brand-sample" type="text" placeholder="For example: an afternoon walk" autocomplete="off">

[Review component roles](plectara-color-migration.md){ .md-button .md-button--primary }
[View brand kit](../01-brand/plectara-brand-kit.md){ .md-button }

<p class="success">✓ Success: your sample is ready.</p>
<p class="warning">! Warning: an entry needs review.</p>
<p class="critical">× Error: a required value is missing.</p>
<p class="ai">AI-assisted explanation — purple is reserved for AI meaning.</p>

</div>

See the [contrast results](plectara-contrast-report.md) for the tested foreground/background combinations. Labels and symbols remain necessary; color is not the only indication of state.

## Component states

These local samples illustrate the [dark mode standard](dark-mode.md). Use the header's theme switch, keyboard Tab navigation, and browser zoom to inspect both themes. The controls do not save or submit data.

<div class="plectara-preview plectara-state-grid">
  <section>
    <h3>Inputs and recovery</h3>
    <label for="dark-sample-hint">Note</label>
    <input id="dark-sample-hint" placeholder="For example: an afternoon walk" autocomplete="off">
    <label for="dark-sample-error">Duration in minutes</label>
    <input id="dark-sample-error" value="-5" aria-invalid="true" aria-describedby="dark-sample-error-help" readonly>
    <p id="dark-sample-error-help" class="critical">! Enter a duration greater than zero. This is a fixed validation example.</p>
    <p class="secondary">Supporting text stays readable in either theme.</p>
  </section>
  <section>
    <h3>Selection and actions</h3>
    <label class="plectara-choice"><input type="checkbox" checked> Include this note in my summary</label>
    <p><button type="button" class="md-button md-button--primary">Save note</button></p>
    <p><button type="button" class="md-button" disabled aria-describedby="sample-disabled-reason">Continue</button></p>
    <p id="sample-disabled-reason" class="secondary">Complete the required information to continue.</p>
    <p><a href="../dark-mode/">Read the dark mode guidelines</a></p>
  </section>
</div>

## Health and AI states

<div class="plectara-preview plectara-state-grid">
  <p class="plectara-state-badge success">✓ Success: your note was saved.</p>
  <p class="plectara-state-badge warning">! Warning: check the recorded time.</p>
  <p class="plectara-state-badge critical">! Error: this sample could not be saved.</p>
  <p class="plectara-state-badge ai">✦ AI-assisted explanation</p>
</div>

## Two-series chart

This synthetic example combines distinct line patterns and markers with accessible values. It demonstrates the default two-series treatment; overlapping or stacked data needs additional adjacency review.

<div class="plectara-preview">
  <svg class="plectara-chart-sample" viewBox="0 0 320 140" role="img" aria-labelledby="sample-chart-title sample-chart-desc">
    <title id="sample-chart-title">Sample readings across three days</title>
    <desc id="sample-chart-desc">Series A rises from 3 to 5 to 7. Series B moves from 9 to 8 and stays at 8. Exact values follow in the table.</desc>
    <path class="sample-axis" d="M30 12 V115 H295"/>
    <polyline class="sample-series-primary" points="50,88 160,66 270,44"/>
    <g class="sample-marker-primary"><circle cx="50" cy="88" r="4"/><circle cx="160" cy="66" r="4"/><circle cx="270" cy="44" r="4"/></g>
    <polyline class="sample-series-secondary" points="50,22 160,33 270,33"/>
    <g class="sample-marker-secondary"><rect x="46" y="18" width="8" height="8"/><rect x="156" y="29" width="8" height="8"/><rect x="266" y="29" width="8" height="8"/></g>
    <g class="sample-chart-label"><text x="34" y="135">Day 1</text><text x="144" y="135">Day 2</text><text x="254" y="135">Day 3</text></g>
  </svg>
  <p>Series A: solid line, circles. Series B: dashed line, squares. Unit: sample points.</p>
</div>

| Day | Series A | Series B |
| --- | --- | --- |
| 1 | 3 | 9 |
| 2 | 5 | 8 |
| 3 | 7 | 8 |

The [component contrast report](plectara-component-contrast-report.md) measures the specified color roles. Rendered behavior and assistive technology still require review in the consuming app.
