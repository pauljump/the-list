# Agents

96,129 subagents: every distinct `agents/*.md` the crawl could read, with what it is for.

## Get it

- [`agents.csv`](agents.csv) (42 MB)

Columns: `name`, `description`, `repo`, `url`, `stars`, `license`, `last_pushed`, `copies`, `tools`, `model`.

## Notes

- The crawl found 250,457 of these files across all repos; 178,392 are distinct. The text of 112,292 was read; 66,100 could not be (too large, binary, or gone from GitHub).
- Entries with the same name and description are one entry, shown at the most-starred repo that is not a fork. `copies` is how many copies of the file the crawl found across GitHub.
- 95,714 have a description: the file's own `description`, or its first paragraph when it has none. Cut at 600 characters.
- `stars`, `license` and `last_pushed` belong to the repo.
- Any Markdown file in an `agents/` folder counts, so agents written for Copilot, Codex and others are included.

## Browse

- [0-9-001](0-9-001.md): 1,121 entries, $(echo $agent | sed 's/-/ /g' | sed 's/\b\(.\)/\u… to 🧪 tester
- [a-001](a-001.md): 893 entries, a to ado-devops-assistant
- [a-002](a-002.md): 936 entries, ado-discovery to agent-session
- [a-003](a-003.md): 1,009 entries, agent-session-reviewer to aiox-analyst
- [a-004](a-004.md): 901 entries, aiox-analyst to animations-specialist
- [a-005](a-005.md): 950 entries, animator to apply-assessment-prep
- [a-006](a-006.md): 1,001 entries, apply-ats-scan to architect-reviewer
- [a-007](a-007.md): 852 entries, architect-reviewer to ascent-supabase-architect
- [a-008](a-008.md): 935 entries, ascent-swift-agent to autocode-workflow
- [a-009](a-009.md): 370 entries, autocontext-curator to azurelocal.github.io-engineer
- [b-001](b-001.md): 915 entries, b to bee:backend-engineer-php
- [b-002](b-002.md): 973 entries, bee:best-practices-researcher to brainiac
- [b-003](b-003.md): 968 entries, BRAINSTEM to builder
- [b-004](b-004.md): 407 entries, builder to bz-news-api
- [c-001](c-001.md): 935 entries, C# Expert to champion
- [c-002](c-002.md): 915 entries, change to claim-auditor
- [c-003](c-003.md): 931 entries, claim-auditor to cmake-triage
- [c-004](c-004.md): 898 entries, cmd-agent-select-logic to code-reviewer
- [c-005](c-005.md): 1,015 entries, code-reviewer to code-reviewer
- [c-006](c-006.md): 952 entries, code-reviewer to codex-companion-protocol
- [c-007](c-007.md): 959 entries, codex-consultant to completeness-checker
- [c-008](c-008.md): 918 entries, completeness-checker to contemplative
- [c-009](c-009.md): 942 entries, contemplative to coordinator
- [c-010](c-010.md): 960 entries, coordinator to credential-tester
- [c-011](c-011.md): 942 entries, credit-analyst to cuj-auditor
- [c-012](c-012.md): 292 entries, cuj-author to CzechLawAdvisor
- [d-001](d-001.md): 942 entries, D-storage to database-integrity-agent
- [d-002](d-002.md): 989 entries, database-integrity-validator to decision-archaeologist
- [d-003](d-003.md): 947 entries, decision-auditor to deps-steward
- [d-004](d-004.md): 914 entries, deps-updater to dev-coder
- [d-005](d-005.md): 954 entries, dev-commands to diagnostic-orchestrator
- [d-006](d-006.md): 967 entries, diagnostic-reader to doc-writer
- [d-007](d-007.md): 944 entries, doc-writer to documentation-editor
- [d-008](d-008.md): 986 entries, documentation-engineer to dry-deduplicator
- [d-009](d-009.md): 207 entries, dry-deduplicator to dyspraxia-advocate
- [e-001](e-001.md): 927 entries, E-Commerce Catalog Designer to engagement-hitlist
- [e-002](e-002.md): 953 entries, engagement-manager to evidence-skeptic
- [e-003](e-003.md): 1,015 entries, evidence-summariser to expo-docs
- [e-004](e-004.md): 165 entries, expo-eas-release-ota to Ezri
- [f-001](f-001.md): 957 entries, F-integrator to feature-spec-analyst
- [f-002](f-002.md): 935 entries, feature-spec-reviewer to fixer-max
- [f-003](f-003.md): 890 entries, fixer-medium to framework-review-agent
- [f-004](f-004.md): 914 entries, framework-reviewer to fullstack-developer
- [f-005](f-005.md): 190 entries, fullstack-developer to fyodor
- [g-001](g-001.md): 927 entries, g1 to general-task
- [g-002](g-002.md): 929 entries, general-technical-project-lead to go-performance-reviewer
- [g-003](g-003.md): 945 entries, go-pr-reviewer to growth-marketer
- [g-004](g-004.md): 393 entries, growth-marketer to gz-qa-engineer
- [h-001](h-001.md): 907 entries, h22-adjudicator to history-reader
- [h-002](h-002.md): 467 entries, history-reviewer to hyv-voiceover
- [i-001](i-001.md): 925 entries, i0 to implementer
- [i-002](i-002.md): 967 entries, implementer to instruction-advisor
- [i-003](i-003.md): 889 entries, instruction-block-updater to Issue Tracker
- [i-004](i-004.md): 487 entries, Issue Triage to ixian
- [j-001](j-001.md): 636 entries, j-flow-architect to jwt-expert
- [k-001](k-001.md): 933 entries, k to kw-distiller
- [k-002](k-002.md): 16 entries, kw-fetcher to kyzo-plan-task-completion-judge
- [l-001](l-001.md): 906 entries, L001-2 to legal-sanitizer
- [l-002](l-002.md): 903 entries, legal-team to Load Test Generator Agent
- [l-003](l-003.md): 493 entries, Load Testing to Lyssandria
- [m-001](m-001.md): 931 entries, m to mcp-expert
- [m-002](m-002.md): 943 entries, mcp-expert to mgmt-dean
- [m-003](m-003.md): 951 entries, mgr-claude-code-bible to model-debugger
- [m-004](m-004.md): 880 entries, model-designer to mz-verifier
- [n-001](n-001.md): 908 entries, n1-hunter to notification-quality
- [n-002](n-002.md): 310 entries, notification-router to nyx
- [o-001](o-001.md): 951 entries, O'Brien to optimera
- [o-002](o-002.md): 951 entries, optimist to overseer
- [o-003](o-003.md): 56 entries, overseer to oyakata-neko
- [p-001](p-001.md): 924 entries, p1-agent to perf-auditor
- [p-002](p-002.md): 968 entries, perf-auditor to phish
- [p-003](p-003.md): 941 entries, phishing-operator to plane-expert
- [p-004](p-004.md): 994 entries, plane-sprint-planner to plugin-shape-reviewer
- [p-005](p-005.md): 943 entries, plugin-smith to pr-commenter-batch
- [p-006](p-006.md): 937 entries, pr-communication-agent to privacy-reviewer
- [p-007](p-007.md): 902 entries, privacy-reviewer to project-bootstrapper
- [p-008](p-008.md): 918 entries, project-capture to prune-agent
- [p-009](p-009.md): 586 entries, prune-blind-reader to pz-server-dev
- [q-001](q-001.md): 972 entries, q to qrspi-plan-test-coverage-reviewer
- [q-002](q-002.md): 542 entries, qrspi-questions-reviewer to qx-partner
- [r-001](r-001.md): 1,027 entries, R-adversarial to README
- [r-002](r-002.md): 1,071 entries, README to refactor-cleaner
- [r-003](r-003.md): 961 entries, refactor-cleaner to repair-coordinator
- [r-004](r-004.md): 893 entries, repair-planner to research-mode.agent
- [r-005](r-005.md): 954 entries, research-model-developer to revenue-chargemaster-analyst
- [r-006](r-006.md): 1,013 entries, revenue-contract-analyst to reviewer
- [r-007](r-007.md): 1,028 entries, reviewer to root-cause-investigator
- [r-008](r-008.md): 655 entries, root-cause-investigator to ryzome-context
- [s-001](s-001.md): 979 entries, S0+S2 × paper × 30 seeds → first populated VALIDA… to scope-creep-reviewer
- [s-002](s-002.md): 947 entries, scope-critic to securable-builder
- [s-003](s-003.md): 974 entries, securable-builder to security-reviewer
- [s-004](s-004.md): 947 entries, security-reviewer to senior-business-analyst
- [s-005](s-005.md): 923 entries, senior-business-analyst-compact to shared-constraints
- [s-006](s-006.md): 905 entries, shared-constraints to skill-improver
- [s-007](s-007.md): 893 entries, skill-improver to solution-architect
- [s-008](s-008.md): 922 entries, solution-architect to spec-risk
- [s-009](s-009.md): 991 entries, spec-runner to stakeholder
- [s-010](s-010.md): 947 entries, stakeholder-advisor to strudel-groove-critic
- [s-011](s-011.md): 949 entries, strudel-harmony-theorist to swiss-case-strategist
- [s-012](s-012.md): 427 entries, swiss-judicial-analyst to Szeth
- [t-001](t-001.md): 771 entries, T'Challa to tapps-validator
- [t-002](t-002.md): 961 entries, taq-wrds-expert to team-runner
- [t-003](t-003.md): 932 entries, team-secretary to test-analyst
- [t-004](t-004.md): 992 entries, test-analyst to test-runner
- [t-005](t-005.md): 1,003 entries, test-runner to theory-verifier
- [t-006](t-006.md): 963 entries, therapist to trellis-check
- [t-007](t-007.md): 754 entries, trellis-check to tzevaadom-alerts.NOTES
- [u-001](u-001.md): 888 entries, uaa2-protocol to url-context-validator
- [u-002](u-002.md): 533 entries, url-grammar-validator to uygulama-ajansi
- [v-001](v-001.md): 988 entries, v-memory to version-numbers
- [v-002](v-002.md): 744 entries, version-prompt to vyroscan-auditor
- [w-001](w-001.md): 916 entries, W18 synthesis — A+B+F findings + W19-W22 roadmap… to wikibot
- [w-002](w-002.md): 978 entries, wikijs-graphql-orchestrator to wta-visualizer
- [w-003](w-003.md): 33 entries, wtfp-argument-verifier to wz:code-reviewer
- [x-001](x-001.md): 109 entries, x to xy-coach
- [y-001](y-001.md): 123 entries, yaat-explore to yytoolkit-provenance
- [z-001](z-001.md): 118 entries, z-audit to zymtrace-perf-engineer
