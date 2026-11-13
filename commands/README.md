# Commands

130,136 slash commands: every distinct `commands/*.md` the crawl could read.

## Get it

- [`commands.csv`](commands.csv) (38 MB)

Columns: `name`, `description`, `repo`, `url`, `stars`, `license`, `last_pushed`, `copies`, `argument_hint`, `allowed_tools`, `model`.

## Notes

- The crawl found 244,879 of these files across all repos; 167,277 are distinct. The text of 141,963 was read; 25,314 could not be (too large, binary, or gone from GitHub).
- Entries with the same name and description are one entry, shown at the most-starred repo that is not a fork. `copies` is how many copies of the file the crawl found across GitHub.
- 129,714 have a description: the file's own `description`, or its first paragraph when it has none. Cut at 600 characters.
- `stars`, `license` and `last_pushed` belong to the repo.
- `name` is the file name, which is what you type after the slash.

## Browse

- [0-9-001](0-9-001.md): 729 entries, # AgentPane Phase 1: Foundation Layer to 프로젝트시작
- [a-001](a-001.md): 1,481 entries, a to add-test
- [a-002](a-002.md): 1,411 entries, add-test to agent-oracle-codex
- [a-003](a-003.md): 1,410 entries, agent-oracle-gemini to analysis
- [a-004](a-004.md): 1,454 entries, analysis to apply
- [a-005](a-005.md): 1,422 entries, apply to ask
- [a-006](a-006.md): 1,428 entries, ask to audit-formalisation
- [a-007](a-007.md): 1,353 entries, audit-freshness to azure-tenant-setup
- [b-001](b-001.md): 1,502 entries, b to blueprint-optimize
- [b-002](b-002.md): 1,417 entries, blueprint-plan to broken-ref
- [b-003](b-003.md): 1,473 entries, broker to builder-write-test
- [b-004](b-004.md): 297 entries, buildforce.build to bzpopmin
- [c-001](c-001.md): 1,651 entries, c to carve-codesight
- [c-002](c-002.md): 1,604 entries, carve-commit to check-architecture
- [c-003](c-003.md): 1,522 entries, check-architecture to claim
- [c-004](c-004.md): 1,458 entries, claim to coach
- [c-005](c-005.md): 1,411 entries, coach to commit
- [c-006](c-006.md): 1,541 entries, commit to component
- [c-007](c-007.md): 1,439 entries, component to context-refresh
- [c-008](c-008.md): 1,449 entries, context-refresh to cowork-add
- [c-009](c-009.md): 1,424 entries, cowork-add-area to create-skill-parent
- [c-010](c-010.md): 1,309 entries, create-skills-via-llms to curate-questions
- [c-011](c-011.md): 276 entries, curate-recall to cypher
- [d-001](d-001.md): 1,517 entries, d to debug-session
- [d-002](d-002.md): 1,490 entries, debug-session to deploy-checklist
- [d-003](d-003.md): 1,348 entries, deploy-checklist to destroy
- [d-004](d-004.md): 1,485 entries, destroy to discover-profiles
- [d-005](d-005.md): 1,444 entries, discover-project-semantics to doctor
- [d-006](d-006.md): 1,413 entries, doctor to dw-flow
- [d-007](d-007.md): 197 entries, dw-functional-doc to dz-verify-step
- [e-001](e-001.md): 1,478 entries, e to epic-swarm
- [e-002](e-002.md): 1,454 entries, epic-sync to experiment-design
- [e-003](e-003.md): 885 entries, experiment-formalisation to eye-health
- [f-001](f-001.md): 1,431 entries, f to find
- [f-002](f-002.md): 1,525 entries, find to flow-metrics
- [f-003](f-003.md): 1,525 entries, flow-migrate to functional
- [f-004](f-004.md): 123 entries, functional-fatigue-budget to fzf-theme
- [g-001](g-001.md): 1,419 entries, g to generate-sns-profile
- [g-002](g-002.md): 1,494 entries, generate-social to goal-setting
- [g-003](g-003.md): 1,331 entries, goal-spec-tasks to gz:wf
- [h-001](h-001.md): 1,483 entries, h to help
- [h-002](h-002.md): 1,419 entries, help to hyrex-swarm
- [i-001](i-001.md): 1,423 entries, i-audit to improve-codebase-architecture
- [i-002](i-002.md): 1,487 entries, improve-codebase-architecture to init-mcp
- [i-003](i-003.md): 1,448 entries, init-mcp-server to inversion
- [i-004](i-004.md): 648 entries, inversion-dtd to izap-mcp-client
- [j-001](j-001.md): 733 entries, j to jyl-usage
- [k-001](k-001.md): 1,069 entries, k-exaone to kztek-brand-info
- [l-001](l-001.md): 1,467 entries, l to linear-my-issues
- [l-002](l-002.md): 1,504 entries, linear-new to login
- [l-003](l-003.md): 699 entries, login to lyrics
- [m-001](m-001.md): 1,421 entries, m to mediavortex-analyze-transcode
- [m-002](m-002.md): 1,444 entries, mediavortex-check-baselines to migrate
- [m-003](m-003.md): 1,389 entries, migrate to monodesign-craft
- [m-004](m-004.md): 871 entries, monodesign-critique to myunsw
- [n-001](n-001.md): 1,517 entries, n to nextjs-fix
- [n-002](n-002.md): 909 entries, nextjs-init to nz-business-english
- [o-001](o-001.md): 1,490 entries, o2-status to openui-install
- [o-002](o-002.md): 1,263 entries, openui-integrate to oxytocin
- [p-001](p-001.md): 1,424 entries, p to personas
- [p-002](p-002.md): 1,526 entries, personas to plan
- [p-003](p-003.md): 1,453 entries, plan to polish
- [p-004](p-004.md): 1,487 entries, polish to prd-to-issues
- [p-005](p-005.md): 1,414 entries, prd-to-json to progress
- [p-006](p-006.md): 1,377 entries, progress to psm
- [p-007](p-007.md): 677 entries, psm to pz-server-tool
- [q-001](q-001.md): 1,146 entries, q to qwik-expert
- [r-001](r-001.md): 1,441 entries, r to ready-check
- [r-002](r-002.md): 1,484 entries, ready-for-main to refine
- [r-003](r-003.md): 1,464 entries, refine to remove
- [r-004](r-004.md): 1,447 entries, remove to research-lib
- [r-005](r-005.md): 1,516 entries, research-library to review
- [r-006](r-006.md): 1,565 entries, review to review-community
- [r-007](r-007.md): 1,392 entries, review-community-health to risk-assessment
- [r-008](r-008.md): 1,479 entries, risk-assessment to run-quarterly-cycle
- [r-009](r-009.md): 375 entries, run-quarterly-planning to rx-report
- [s-001](s-001.md): 1,455 entries, s to scene
- [s-002](s-002.md): 1,461 entries, scene to seclabel.h
- [s-003](s-003.md): 1,420 entries, second-brain to service-health-watchlist
- [s-004](s-004.md): 1,565 entries, service-inventory to setup
- [s-005](s-005.md): 1,439 entries, setup to shotgun
- [s-006](s-006.md): 1,447 entries, should-i-start-fresh to smith:tax
- [s-007](s-007.md): 1,417 entries, smm to specify
- [s-008](s-008.md): 1,419 entries, specify to stack
- [s-009](s-009.md): 1,524 entries, stack to status
- [s-010](s-010.md): 1,671 entries, status to stripe-test
- [s-011](s-011.md): 1,470 entries, strix-apply to sync-check
- [s-012](s-012.md): 546 entries, sync-check to szukaj
- [t-001](t-001.md): 1,485 entries, t to tech-writer
- [t-002](t-002.md): 1,589 entries, tech-writer to testarch-ci
- [t-003](t-003.md): 1,469 entries, testarch-ci to trace
- [t-004](t-004.md): 1,443 entries, trace to tz
- [u-001](u-001.md): 1,462 entries, UA Analyze to update-epic
- [u-002](u-002.md): 1,077 entries, update-epic to uzman-guncelle
- [v-001](v-001.md): 1,512 entries, v to verify
- [v-002](v-002.md): 1,241 entries, verify to vyroscan-audit
- [w-001](w-001.md): 1,469 entries, w to wip
- [w-002](w-002.md): 1,383 entries, wip to write-plan
- [w-003](w-003.md): 359 entries, write-plan to wyatt
- [x-001](x-001.md): 141 entries, x to xyz
- [y-001](y-001.md): 145 entries, y-govern to yuri-zenkai
- [z-001](z-001.md): 156 entries, z-audit to zzzprobe
