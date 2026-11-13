# Agents

27,720 subagents: every distinct `agents/*.md` the crawl could read, with what it is for.

## Get it

- [`agents.csv`](agents.csv) (12 MB)

Columns: `name`, `description`, `repo`, `url`, `stars`, `license`, `last_pushed`, `copies`, `tools`, `model`.

## Notes

- The crawl found 192,389 of these files across all repos; 143,960 are distinct. The text of 32,106 was read; 111,854 could not be (too large, binary, or gone from GitHub).
- Entries with the same name and description are one entry, shown at the most-starred repo that is not a fork. `copies` is how many copies of the file the crawl found across GitHub.
- 27,649 have a description: the file's own `description`, or its first paragraph when it has none. Cut at 600 characters.
- `stars`, `license` and `last_pushed` belong to the repo.
- Any Markdown file in an `agents/` folder counts, so agents written for Copilot, Codex and others are included.

## Browse

- [0-9-001](0-9-001.md): 198 entries, .NET Self-Learning Architect to 需求规划师
- [a-001](a-001.md): 939 entries, a to amphibious-explore
- [a-002](a-002.md): 916 entries, amphibious-verify to arn-spark-product-strategist
- [a-003](a-003.md): 494 entries, arn-spark-prototype-builder to azure-to-docker-expert
- [b-001](b-001.md): 892 entries, B-shell to byzantine-coordinator
- [c-001](c-001.md): 933 entries, C# Expert to code-craftsman
- [c-002](c-002.md): 973 entries, code-critic to Compliance Checker
- [c-003](c-003.md): 953 entries, Compliance Grounding Agent to crm-hygiene-agent
- [c-004](c-004.md): 392 entries, crm-manager to cytoscape.js_agents
- [d-001](d-001.md): 945 entries, D-storage to design-quality-reviewer
- [d-002](d-002.md): 937 entries, design-quality-reviewer to document-specialist
- [d-003](d-003.md): 373 entries, document-summarizer to Dyrygent systemu wieloagentowego
- [e-001](e-001.md): 817 entries, E-Commerce Catalog Designer to eye
- [f-001](f-001.md): 927 entries, F-integrator to frontend-designer
- [f-002](f-002.md): 179 entries, frontend-designer to fyodor
- [g-001](g-001.md): 972 entries, g1 to gsd-ui-researcher
- [g-002](g-002.md): 40 entries, gsd-ui-researcher to gyoshu
- [h-001](h-001.md): 469 entries, ha-addon-developer to hyv-voiceover
- [i-001](i-001.md): 866 entries, i0 to iwubi_agents
- [j-001](j-001.md): 185 entries, james-architect to jwt-expert
- [k-001](k-001.md): 320 entries, k8s-argocd-health-agent to kyc-screener
- [l-001](l-001.md): 671 entries, l10n-auditor to Lyra
- [m-001](m-001.md): 941 entries, m-a-transaktionsrecht-drafter to morty-phase-implementer
- [m-002](m-002.md): 126 entries, morty-phase-planner to mystic
- [n-001](n-001.md): 442 entries, n8n-author to nyquil
- [o-001](o-001.md): 586 entries, oa_fetcher to ownership-analyst
- [p-001](p-001.md): 931 entries, p1-agent to planner
- [p-002](p-002.md): 935 entries, planner to production-readiness-analyst
- [p-003](p-003.md): 557 entries, production-readiness-checker to pytorch-security-auditing-consultant
- [q-001](q-001.md): 442 entries, q1-research-question to qx-partner
- [r-001](r-001.md): 1,029 entries, r-developer to requirements-definer
- [r-002](r-002.md): 996 entries, requirements-definer-auditor to rust-ci-fixer
- [r-003](r-003.md): 68 entries, rust-cli-architect to rvcsi-engineer
- [s-001](s-001.md): 968 entries, s3-migration-planner to seed-architect
- [s-002](s-002.md): 939 entries, seed-architect to solution-writer
- [s-003](s-003.md): 961 entries, solution_verifier_agent to swift-data-pipelines-advisor
- [s-004](s-004.md): 193 entries, swift-data-reviewer to systems-weaver
- [t-001](t-001.md): 976 entries, ta to test-writer-fixer
- [t-002](t-002.md): 653 entries, test-writer-fixer to typography-expert
- [u-001](u-001.md): 395 entries, uarch-designer to uxaudit-scout
- [v-001](v-001.md): 527 entries, v1 to vyper-specialist
- [w-001](w-001.md): 562 entries, wack to wxpython-specialist
- [x-001](x-001.md): 29 entries, x-content-loop to xy-coach
- [y-001](y-001.md): 32 entries, yak-shave-detector to yt2b-strategist
- [z-001](z-001.md): 41 entries, zai-cli to Zwiadowca Przepisow
