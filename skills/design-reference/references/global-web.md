# Global Web Live Reference

Use Global Web as a live design-research lens. Use it for art direction and interaction ideas, not as a default usability standard or a pixel-cloning target.

## Sources

- Awwwards home: https://www.awwwards.com/
- Websites: https://www.awwwards.com/websites/
- Collections: https://www.awwwards.com/collections/
- Elements: https://www.awwwards.com/elements/
- Recent Design: https://recent.design/
- Dribbble: https://dribbble.com/

Choose the source by the question:

- **Awwwards**: complete live websites, landing pages, portfolios, art direction, typography, motion, and experimental interaction.
- **Recent Design**: broad discovery across web interfaces, branding, product, typography, motion, illustration, 3D, editorial, app screenshots, app icons, and related design tools.
- **Dribbble**: screen-level UI, dashboards, landing pages, mobile apps, onboarding, ecommerce, illustrations, branding, and motion concepts.

These are dynamic platforms. Their examples, popularity signals, categories, access rules, and URLs may change. Inspect the live source for each task. Do not store a scraped catalog in this skill.

## Workflow

1. Define the design question before browsing.
   - Specify the page type: landing page, campaign, portfolio, editorial, commerce, or brand experience.
   - Specify the intended feeling and business action.
   - Set implementation limits for motion, loading cost, devices, browser support, accessibility, SEO, and content maintenance.

2. Search narrowly.
   - Choose one primary source whose format matches the question before searching.
   - On Awwwards, filter by the relevant category, tag, technology, element, or collection.
   - On Recent Design, narrow by discipline such as web interface, branding, product, typography, motion, illustration, 3D, or editorial.
   - On Dribbble, search for the concrete screen or component, such as `SaaS dashboard`, `checkout`, `mobile onboarding`, or `pricing page`.
   - Prefer a concrete question such as `premium product hero`, `editorial typography`, `scroll storytelling`, or `portfolio project transition` over a vague request for a beautiful site.
   - Use awards, likes, views, popularity, and recency only as discovery signals. They do not prove conversion, accessibility, performance, originality, or product fit.
   - Ignore courses, marketplaces, hiring, agency directories, and other commercial areas unless the user asks for them.

3. Compare up to three relevant examples.
   - Choose examples that solve the same communication problem.
   - Prefer meaningful variation in composition, typography, motion intensity, and navigation.
   - Record the source detail URL, original website URL when available, category or tags shown, creator, and the observation date.
   - Inspect the original website or a working prototype when practical because gallery images and isolated shots cannot reveal responsive behavior, interaction states, content constraints, or implementation quality.

4. Extract transferable decisions.
   - Composition: hero structure, grid, rhythm, focal point, and content reveal order.
   - Art direction: imagery, color roles, texture, shape language, and visual contrast.
   - Typography: family roles, scale, line length, hierarchy, and responsive behavior.
   - Motion: purpose, trigger, duration, easing, choreography, and reduced-motion fallback.
   - Interaction: navigation model, cursor behavior, scroll effects, transitions, feedback, and escape routes.
   - Implementation: likely CSS, SVG, canvas, WebGL, video, or animation dependencies and their maintenance cost.

5. Apply reality gates.
   - Preserve readable content and conventional navigation where task completion matters.
   - Provide keyboard access, visible focus, sufficient contrast, semantic structure, and reduced-motion behavior.
   - Avoid autoplay audio, scroll hijacking, cursor-only meaning, hidden navigation, or long unskippable intros unless the product context clearly justifies them.
   - Replace heavy 3D, video, or WebGL with lighter fallbacks when the visual payoff does not justify loading and device cost.
   - Keep SEO, localization, content editing, and mobile behavior viable.
   - Treat Dribbble shots and static Recent Design entries as visual hypotheses, not evidence that the full flow works. Add missing loading, empty, error, disabled, focus, and responsive states before implementation.

6. Decide rather than imitate.
   - Mark each idea as `borrow`, `adapt`, or `reject`.
   - Explain how it supports the user's message and conversion goal.
   - Rebuild the selected grammar with original copy, assets, components, and project-native tokens.

7. Verify the implementation.
   - Check desktop and mobile layouts, keyboard flow, reduced motion, text readability, loading behavior, and interaction fallbacks.
   - Verify that the main message and primary action remain clear before and without animation.
   - Compare the result against the design decisions, not against screenshot-level similarity.

## Avoid or Use Sparingly

Use Korea UI or a restrained local brand reference first for dense dashboards, CRMs, admin tools, checkout, authentication, settings, data entry, and other task-heavy flows. Add Global Web only for a bounded expressive surface such as a marketing hero or campaign module.

## Copyright and Attribution Guardrails

- Treat screenshots, videos, logos, copy, fonts, illustrations, and code as belonging to their respective rights holders.
- Do not bulk-download, mirror, redistribute, or bundle Awwwards, Recent Design, Dribbble, or featured-site content.
- Do not copy proprietary source code, branded assets, or marketing copy into the user's project.
- Recreate only general composition, interaction principles, or design grammar with original content and authorized assets.
- Keep the source detail URL, creator attribution, and original website URL when available in the design brief or final report.

## Output Template

Use this compact structure before implementation:

```markdown
### Global Web reference decision

- Problem: <page type and communication goal>
- Sources: <Awwwards, Recent Design, or Dribbble detail links and original-site links>
- Borrow: <ideas to retain>
- Adapt: <ideas to simplify or localize and why>
- Reject: <ideas that harm usability, accessibility, or performance>
- Project rules: <layout, type, motion, technology, and fallback constraints>
- Verification: <desktop, mobile, keyboard, reduced-motion, and loading checks>
```

If relevant content is unavailable, report the access limitation and continue with local brand references or user-provided screenshots. Do not invent examples that were not observed.
