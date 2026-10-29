# Korea UI Live Reference

Use Korea UI as a live Korean product-pattern research lens, not as an asset library or a pixel-cloning target. Its current source site is UI Bowl.

## Sources

- UI Bowl: https://uibowl.io/
- First-use guide: https://blossom-browser-536.notion.site/32cbc17e43118043b8e8e2c20a31b2f9

UI Bowl is a dynamic site whose categories, examples, access rules, and URLs may change. Inspect the live site for each task. Do not store a scraped catalog in this skill.

## Workflow

1. Define the reference question before browsing.
   - Specify platform: mobile, website, or game.
   - Specify the screen, flow, component, or interaction to solve.
   - Note product audience, device constraints, accessibility needs, and the project's existing design system.

2. Search narrowly.
   - Use the source site's visible search and filters when browser access is available.
   - Prefer an exact product problem such as `간편결제`, `검색`, `온보딩`, or `필터` over a vague mood word.
   - Use MAU and popularity only as discovery signals. They do not prove usability or suitability.
   - Do not bypass login, membership, paywalls, rate limits, or other access controls.

3. Compare up to three relevant examples.
   - Choose examples that solve the same user task, not merely examples with similar colors.
   - Prefer meaningful variation: one conventional pattern, one dense or power-user pattern, and one simplified pattern when available.
   - Record each product name, source URL, platform, pattern name, and the observation date.

4. Extract design decisions.
   - Information hierarchy: what appears first, what is grouped, and what is progressively disclosed.
   - Navigation: entry point, back path, tabs, steps, and escape routes.
   - Components and states: default, loading, empty, error, success, disabled, and destructive states.
   - Interaction: tap or click target, gesture, animation purpose, feedback, and recovery.
   - Visual grammar: density, spacing rhythm, type hierarchy, color roles, radii, elevation, and imagery.
   - Accessibility risks: contrast, target size, color-only meaning, motion, text scaling, keyboard flow, and screen-reader labels.

5. Decide rather than average.
   - Mark each useful idea as `borrow`, `adapt`, or `reject`.
   - Explain why it fits or conflicts with the user's audience, content, product goals, and current codebase.
   - Convert the selected ideas into project-native components and tokens.

6. Verify the implementation.
   - Check the implemented flow at relevant desktop and mobile sizes.
   - Verify overflow, contrast, touch targets, keyboard focus, loading and empty states, and interaction feedback.
   - Compare the result against the design decisions, not against screenshot-level visual similarity.

## Copyright and Attribution Guardrails

- Treat screenshots, logos, copy, illustrations, and other displayed content as belonging to their respective rights holders.
- Do not bulk-download, mirror, redistribute, or bundle UI Bowl content.
- Do not paste third-party screenshots or branded assets into deliverables unless the user has the necessary rights and explicitly requests it.
- Recreate only the general layout logic, interaction pattern, or design grammar using original content and project-native assets.
- Keep source links in the design brief or final report so the inspiration remains traceable.

## Output Template

Use this compact structure before implementation:

```markdown
### Reference decision

- Problem: <screen, flow, component, or interaction>
- Sources: <Korea UI source links and optional brand DESIGN.md>
- Borrow: <ideas to retain>
- Adapt: <ideas to change and why>
- Reject: <ideas that conflict with this product>
- Project rules: <tokens, components, states, accessibility constraints>
- Verification: <viewport and interaction checks>
```

If the relevant Korea UI source content is unavailable, report the access limitation and continue with the local brand references or user-provided screenshots. Do not invent examples that were not observed.
