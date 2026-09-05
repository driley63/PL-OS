# CSS token integration

Import the generated adapter instead of duplicating palette values.

```css
@import "./plectara-tokens.css";

.primary-action {
  background: var(--plectara-button-primary-background);
  color: var(--plectara-button-primary-label);
  border-color: var(--plectara-button-primary-background);
}
.primary-action:hover {
  background: var(--plectara-button-primary-hover);
}
.primary-action:focus-visible {
  outline: 3px solid var(--plectara-focus-ring);
  outline-offset: 3px;
}
```

Set `data-theme="dark"` on the application root for dark semantic roles; remove it for light mode. Keep the component library's existing padding, sizing, radii, disabled behavior, and interaction rules.

See the [interactive color preview](../../02-design/plectara-component-preview.md).
