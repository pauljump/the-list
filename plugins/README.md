# Plugins

113,195 Claude Code plugins: every entry of every `.claude-plugin/marketplace.json` the crawl found, with what it does, where it lives and what is inside it.

## Get it

- [`plugins.csv`](plugins.csv) (40 MB)

Columns: `name`, `description`, `category`, `keywords`, `version`, `repo`, `url`, `stars`, `license`, `last_pushed`, `skills`, `commands`, `agents`, `hook_files`, `mcp_configs`, `marketplace_repo`, `marketplace_name`, `marketplaces`, `copies`, `repo_gone`.

## Notes

- Built from 135,679 marketplace entries. A plugin listed in several marketplaces appears once; copies with the same name and description under other repos (forks, mirrors) are folded into the original (`copies`).
- 101,356 have a description, in the author's words, cut at 600 characters. 3,189 of those were blank in the marketplace and filled from the plugin's own `plugin.json` or its repo description.
- `skills`, `commands`, `agents`, `hook_files`, `mcp_configs` count the files found under the plugin's folder.
- To install one: `/plugin marketplace add <marketplace_repo>` then `/plugin install <name>@<marketplace_name>`.
- 3,539 point at a repo that was already deleted or renamed at crawl time (`repo_gone`).
- `stars`, `license` and `last_pushed` belong to the repo, not the plugin.

## Browse

- [0-9-001](0-9-001.md): 408 entries, .NET Backend Patterns to 通用技能
- [a-001](a-001.md): 1,326 entries, a to aerospike-ce-ecosystem
- [a-002](a-002.md): 1,315 entries, aes-skills to agent-team
- [a-003](a-003.md): 1,312 entries, agent-team to ai-canvas
- [a-004](a-004.md): 1,310 entries, ai-career-roadmap-skill to alexanderop-claude-code-builder
- [a-005](a-005.md): 1,283 entries, alexanderop-claude-skill-vue-development to AntV Chart Visualization
- [a-006](a-006.md): 1,279 entries, antv-g2-chart to arc-code-intelligence
- [a-007](a-007.md): 1,298 entries, arc-conventions to atlassian-pm
- [a-008](a-008.md): 1,318 entries, atlassian-rovo to axe-audit
- [a-009](a-009.md): 271 entries, axe-fix to azzist
- [b-001](b-001.md): 1,335 entries, b to bigquery-pipeline-audit
- [b-002](b-002.md): 1,337 entries, bigquery-zh to brand-kit-os-leafpad
- [b-003](b-003.md): 1,140 entries, brand-landingpage to byunk-claude-code-toolkit
- [c-001](c-001.md): 1,379 entries, c to cc0-audio
- [c-002](c-002.md): 1,358 entries, cc10x to cicd-automation
- [c-003](c-003.md): 1,300 entries, cicd-automation-2 to claude-ecosystem
- [c-004](c-004.md): 1,318 entries, claude-ecosystem-health to ClaudeKit Extensions
- [c-005](c-005.md): 1,352 entries, claudekit-frontend-design-pro-demo to Code Review & Refactor
- [c-006](c-006.md): 1,361 entries, Code Review Analysis to coding-academy
- [c-007](c-007.md): 1,313 entries, coding-aegis to computer-vision-expert
- [c-008](c-008.md): 1,317 entries, computer-vision-pipeline to copier-bootstrap-plugin
- [c-009](c-009.md): 1,296 entries, copier-pyproject to crew
- [c-010](c-010.md): 1,089 entries, crew to czsc-chan-theory
- [d-001](d-001.md): 1,358 entries, d to ddev-tools
- [d-002](d-002.md): 1,320 entries, ddex-delivery to design
- [d-003](d-003.md): 1,273 entries, design to Developer Slides
- [d-004](d-004.md): 1,278 entries, Developer Toolkit to dispatch
- [d-005](d-005.md): 1,334 entries, dispatch to dotkit
- [d-006](d-006.md): 870 entries, dotlight-skillset to dzaleka-online-services-api
- [e-001](e-001.md): 1,309 entries, e-colleagues to engineering-conventions
- [e-002](e-002.md): 1,254 entries, engineering-core to everything-claude-code
- [e-003](e-003.md): 759 entries, everything-claude-code to ezsub
- [f-001](f-001.md): 1,309 entries, f-awesome-chatgpt-prompts-1 to File Ownership Transfer
- [f-002](f-002.md): 1,385 entries, File Test Bug Analyzer to FoBiS
- [f-003](f-003.md): 1,332 entries, focs-skills to full-skills
- [f-004](f-004.md): 261 entries, Full-Stack Developer Agents to fzymgc-house-fzymgc-house-skills
- [g-001](g-001.md): 1,392 entries, g to ghost-writer
- [g-002](g-002.md): 1,412 entries, ghost-writer to glow
- [g-003](g-003.md): 1,368 entries, glow-dev to great-researchers-dxt
- [g-004](g-004.md): 880 entries, great-web-copy to gzp
- [h-001](h-001.md): 1,393 entries, h-level-docs to hex-grid
- [h-002](h-002.md): 1,236 entries, hex-pack to hugo
- [h-003](h-003.md): 501 entries, hugo to hzt
- [i-001](i-001.md): 1,270 entries, i to inkwell
- [i-002](i-002.md): 1,272 entries, inkwell-hooks to izmailov
- [j-001](j-001.md): 1,367 entries, j-flow to jti-reports
- [j-002](j-002.md): 325 entries, jtmthf-skills to jz-tanstack-ship
- [k-001](k-001.md): 1,307 entries, k-dense-ai-claude-scientific-skills to Kotlin Development Prompts
- [k-002](k-002.md): 326 entries, Kotlin Exposed Patterns to kyzo-python
- [l-001](l-001.md): 1,304 entries, l-lawliet to lesson
- [l-002](l-002.md): 1,337 entries, Lesson Learned Tracker to loamkit
- [l-003](l-003.md): 949 entries, loan-officer-assistant to lz-advisor
- [m-001](m-001.md): 1,275 entries, m to marketing-studio
- [m-002](m-002.md): 1,380 entries, marketing-studio to melvynx-aiblueprint
- [m-003](m-003.md): 1,331 entries, melxis to mineru-refine
- [m-004](m-004.md): 1,330 entries, mineru98-llm-proxy-skills to motion
- [m-005](m-005.md): 874 entries, motion to mzizzi-ty-lsp
- [n-001](n-001.md): 1,274 entries, n to nika
- [n-002](n-002.md): 1,118 entries, nika-skills to nzism-tanaji-hemant-naik
- [o-001](o-001.md): 1,397 entries, o to opalite-medical-translator
- [o-002](o-002.md): 1,300 entries, opaque-blob-guard to organizar-fluxo
- [o-003](o-003.md): 565 entries, Organization & RBAC Setup to ozma
- [p-001](p-001.md): 1,322 entries, p to perception-and-hierarchy-principles
- [p-002](p-002.md): 1,369 entries, perception-first-design to planflow
- [p-003](p-003.md): 1,375 entries, plangate to pocket-knife
- [p-004](p-004.md): 1,330 entries, pocket-space to prd-writer
- [p-005](p-005.md): 1,261 entries, prd-writer to project-analizer
- [p-006](p-006.md): 1,256 entries, project-analysis to publisher-ad-revenue
- [p-007](p-007.md): 608 entries, publishing to pyzotero
- [q-001](q-001.md): 860 entries, q to qyrusai-assure
- [r-001](r-001.md): 1,324 entries, r to recovery-pipeline
- [r-002](r-002.md): 1,324 entries, recovery-tabletop to research
- [r-003](r-003.md): 1,308 entries, research to risk-reporting
- [r-004](r-004.md): 1,244 entries, risk-reporting to rzpro
- [s-001](s-001.md): 1,214 entries, s to sciris
- [s-002](s-002.md): 1,287 entries, scispark to security-threat-intelligence-analyst
- [s-003](s-003.md): 1,324 entries, security-threat-intelligence-analyst-zh to setup-vscode-swift
- [s-004](s-004.md): 1,349 entries, setup-workflows to siva01c-claude-plugins
- [s-005](s-005.md): 1,387 entries, sivers to slides-suite
- [s-006](s-006.md): 1,272 entries, slides-suite to sparv
- [s-007](s-007.md): 1,358 entries, spatial-audit-engine to start
- [s-008](s-008.md): 1,287 entries, start to summon-pr
- [s-009](s-009.md): 1,349 entries, summon-seer to System Environment Setup
- [s-010](s-010.md): 116 entries, System of Work to sztwiorok-buddy-plugin
- [t-001](t-001.md): 1,334 entries, t-view-automation to technosutra
- [t-002](t-002.md): 1,336 entries, technyan-x-post-generator to thinking-gtd
- [t-003](t-003.md): 1,421 entries, thinking-habit to topy-ai-operations
- [t-004](t-004.md): 1,322 entries, topy-ai-strategy to type-checking-pattern
- [t-005](t-005.md): 207 entries, Type-Driven Development to Tzurot Deployment Guide
- [u-001](u-001.md): 1,316 entries, u to uuid-cli-zh
- [u-002](u-002.md): 128 entries, UUV End-to-End Testing to uzbekcha-spinner
- [v-001](v-001.md): 1,268 entries, v to vigil-alert
- [v-002](v-002.md): 873 entries, vigil-alert-2 to vz
- [w-001](w-001.md): 1,324 entries, W&B Plot Skill to whatsup
- [w-002](w-002.md): 1,304 entries, whatsup to worktrees
- [w-003](w-003.md): 585 entries, worktrees to wzkariampuzha-claude-skills
- [x-001](x-001.md): 606 entries, x to xyo-skills
- [y-001](y-001.md): 545 entries, y-context7 to yzmir-training-optimization
- [z-001](z-001.md): 562 entries, z to zzzprobe
