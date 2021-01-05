# Project statistics

| Project on Github | total number of jobs | number of unsuccessful* jobs |
|------------------------|----------------------|-----------------------------|
| rails/rails |  471416  |  262918 (55%) |
| jruby/jruby	|  271748 |  58594 (21%)  |
| opf/openproject	| 54992 |  8957   (16%) |
| jruby/activerecord-jdbc-adapter |  51585	| 14765  (28%) |
| rollbar/rollbar-gem | 49968	|   9573   (19%) |
| rspec/rspec-rails	| 44397 | 12358  (27%) |
| slim-template/slim  | 43819 	| 16142  (36%) |
| ruby/ruby	| 34409 |   17045  (49%) |
| diaspora/diaspora	|  32393 |  16317  (50%) |
| SonarSource/sonarqube	| 30142 | 4599   (15%) |

* Any status other than 'ok' which are 'failed', 'unknown', or 'errored'. 


Travis Torrent database Structure

It has only one table.

Data Description

| Column | Description |
| ----------- | ------ |
| tr_job_id | The job id of the build job under analysis. |
| tr_build_id |	The analyzed build id, as reported from Travis CI. |
| gh_project_name |	Project name on GitHub.  |
| git_branch |	The branch that was built |
| tr_status |	The build status (such as passed, failed, …) as returned from the Travis CI API. |
| gh_commits_in_push | The commits included in the push that triggered the build. In rare cases, GHTorrent has not recorded a push event for the commit that created the build in which case gh_commits_in_push is “” (empty string).|
| gh_build_started_at | Timestamp of the push that triggered the build (Travis provided), in UTC. |
| git_all_built_commits | A list of all commits that were built for this build, up to but excluding the commit of the previous build, or up to and including a merge commit (in which case we cannot go further backward).|
| git_trigger_commit | The commit that triggered the build.|
| gh_num_issue_comments | If git_commit is linked to a PR on GitHub, the number of discussion comments on that PR. |


Complete list of database columns:
https://travistorrent.testroots.org/page_dataformat/#data-description
