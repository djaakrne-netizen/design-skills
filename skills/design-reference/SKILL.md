---
name: design-reference
description: Use local brand references plus live Korea UI, Global Web, saved Figma kits, and implementation-ready code-component sources to choose and translate visual language into a UI implementation. Use when the user asks for design inspiration, Korea UI or UI Bowl references, Awwwards, Recent Design, Dribbble, or Global Web references, Figma or HeroUI components, Select Codes or motion UI code, shadcn/ui, Magic UI, Lucide, or Higgsfield for frontend design and assets, Korean product patterns, global landing-page or portfolio inspiration, a DESIGN.md reference, "make it like Linear/Vercel/Claude/Stripe/Notion/etc.", UI polish direction, or a reusable design brief before coding frontend changes.
---

# Design Reference

Use this skill to turn local brand-style references into practical UI direction for Codex work. The goal is not to clone a brand; it is to borrow the design grammar, then adapt it to the user's product, audience, and existing codebase.

## Reference Sources

Bundled source:

- `references/brands/<brand>/DESIGN.md`, relative to this skill directory.
- This package includes 54 brand reference documents from [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md). Read `references/brands/LICENSE` for the upstream license.
- The references can be read offline. Live sites and integrations below still require their own network access and permissions.

Live product-pattern source:

- **Korea UI**: use [UI Bowl](https://uibowl.io/) as the live source for Korean mobile, website, and game UI patterns, components, and interaction references.
- Read `references/korea-ui.md` before using Korea UI. Re-check the live source instead of treating its changing inventory as bundled knowledge.

Live expressive-web source:

- **Global Web**: use [Awwwards](https://www.awwwards.com/) for complete live websites and experimental interaction, [Recent Design](https://recent.design/) for broad cross-disciplinary design discovery, and [Dribbble](https://dribbble.com/) for screen-level UI, component, illustration, and motion concepts.
- Read `references/global-web.md` before using Global Web. Apply its performance, accessibility, and maintainability gates before implementation.

Saved Figma kit source:

- Read `references/figma-kits.md` when the user asks to use Figma, HeroUI, a saved component kit, or a specific Figma component.
- Use the Figma integration to inspect the exact linked node. A whole-file link is suitable for discovery; request or derive a component-specific `node-id` before implementing a component 1:1.

Live code-component source:

- **Select Codes**: use [Select Codes](https://select.codes/) for implementation-ready React, Next.js, Tailwind CSS, and Motion component patterns with live previews and source code.
- Read `references/code-components.md` before using Select Codes. Confirm stack compatibility, dependencies, licensing, accessibility, and reduced-motion behavior before copying or installing code.

Helper resources:

- Run `python3 <skill-directory>/scripts/list_design_refs.py` (replace `<skill-directory>` with the directory containing this SKILL.md) to list available local references.
- Read `references/catalog.md` when the user does not name a brand and you need to choose a fitting style.

AI-readable design and asset sources:

- Read [references/ai-design-tools.md](references/ai-design-tools.md) when selecting or using Figma, shadcn/ui, Magic UI, Lucide, or Higgsfield for frontend work, or when the user asks for MCP-accessible design resources.
- Use Figma for structured design context, shadcn/ui for application components, Magic UI for purposeful motion, Lucide for consistent icons, and Higgsfield for custom image/video assets. Choose only the sources the current task needs.
- Distinguish a service offering MCP from a callable connection in the current session. Adding these sources to this skill does not install or authenticate integrations.

## Workflow

1. Inspect the current project first.
   - Read existing global CSS, Tailwind config, theme tokens, layout components, and representative pages before choosing a reference.
   - If the project already has a strong visual system, adapt the reference lightly instead of replacing the system.

2. Select a reference.
   - If the user names a brand or vibe, use the closest matching local reference.
   - If the user names a screen, flow, component, interaction, Korean product, Korea UI, or UI Bowl, use Korea UI to compare current product examples.
   - If the user names a landing page, campaign, portfolio, brand experience, expressive motion, Global Web, Awwwards, Recent Design, or Dribbble, use Global Web to compare current examples from the most relevant source.
   - If the user names Figma, HeroUI, a component kit, or a specific UI component, check `references/figma-kits.md` and inspect the relevant node through the Figma integration.
   - If the user names Select Codes, motion components, animated cards or tabs, page transitions, or code-first UI inspiration, check `references/code-components.md` and inspect the relevant live component page.
   - If the user needs AI-readable design sources, component retrieval, consistent icons, or generated frontend assets, use `references/ai-design-tools.md`; retain the existing stack and visual system when choosing tools.
   - If the user is vague, choose from `references/catalog.md` based on product type.
   - Prefer the bundled `references/brands/<brand>/DESIGN.md` files for durable project styling.
   - If a brand reference is missing, use an available public source or a reference supplied for the current task; do not assume another local repository exists.
   - Combine at most one structural brand reference with up to three examples from the most relevant live source. Use both Korea UI and Global Web only when the task genuinely spans product flow and expressive marketing.

3. Read only the needed reference.
   - Load one or two relevant brand files, not the whole catalog.
   - Extract colors, typography, spacing, radii, surface treatment, density, component states, and do/don't rules.
   - For Korea UI, record the pattern, information hierarchy, component states, interaction behavior, accessibility risks, and source link. Do not copy screenshots or branded assets into the project.
   - For Global Web, record the composition, art direction, typography, motion purpose, interaction cost, implementation clues, performance risks, accessibility risks, and source link. Do not treat an award score as proof that the pattern fits the user's product.
   - For a Figma kit, inspect component variants, states, variables, typography, spacing, and screenshot before implementation. Reuse the kit's design grammar without assuming its generated code matches the project stack.
   - For a code-component source, record the live behavior, source URL, framework assumptions, dependencies, responsive states, interaction states, accessibility risks, reduced-motion fallback, and license conditions.

4. Translate the reference into the project.
   - Preserve the user's product identity, content, and accessibility needs.
   - Avoid using protected logos, brand names, or copied marketing copy unless the user explicitly owns or requests them.
   - Do not make a pixel clone. Describe the adaptation as "inspired by" or "using the grammar of" the reference.
   - For operational tools, dashboards, CRMs, and internal apps, keep density, scanning, predictable navigation, and restrained styling ahead of decorative composition.

5. Implement using the repo's stack.
   - Use the existing design framework and component patterns.
   - Reuse Select Codes source directly only when its framework and license fit the project. Otherwise translate its visual behavior into the current stack.
   - Do not install component packages or dependencies until their need and compatibility have been checked.
   - If a persistent system is useful, create or update a project-level `DESIGN.md` only when the user asks or the project already uses that pattern.
   - Keep changes scoped to the requested UI surface.

6. Verify visually.
   - For frontend changes, run the app when practical and check a browser screenshot at desktop and mobile sizes.
   - Watch for text overflow, overlapping elements, weak contrast, inconsistent spacing, and mismatched component states.
   - When using Global Web or Select Codes, also verify reduced-motion behavior, keyboard access, loading cost, responsive fallbacks, and readability without animation.

7. Report concisely.
   - Name the reference used.
   - Summarize what was borrowed and what was intentionally changed for this project.
   - Link the Korea UI, Global Web, Figma, or code-component source pages used when applicable.
   - Include verification performed.

## Quick Selection

Use these defaults when the user gives only a product type:

- Developer dashboard or internal tool: `linear.app`, `vercel`, `raycast`, `sentry`
- AI or coding product: `claude`, `cursor`, `warp`, `supabase`, `voltagent`
- Documentation, wiki, or research UI: `mintlify`, `notion`, `replicate`
- Finance, analytics, or trust-heavy product: `stripe`, `coinbase`, `wise`
- Friendly consumer or family app: `airbnb`, `intercom`, `figma`
- Premium object, vehicle, or hardware page: `apple`, `bmw`, `spacex`
- Creative or media-heavy page: `framer`, `runwayml`, `pinterest`, `webflow`
- Expressive marketing, campaign, or portfolio page: use Global Web with one restrained local brand reference.
- React or Next.js interface needing purposeful motion: use Select Codes as the implementation reference with one restrained structural reference.

When in doubt, use one restrained structural reference and one expressive accent reference, then state the blend before implementing.
