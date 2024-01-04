# Introduction 
We need to create a **coding skills assesment tool** which accurately predicts workplace performance.The data gathers 
the static metric for the code written by the developer when attempting a coding assessment 
test and uses it to predict the workplace performance.

Your task is to train a machine learning regression model using the training data provided
and implement a working prediction api 

# Dataset Description
The data column definitions are below

## Independent Variables
  1. Task Name: Name of the task attempted by the developer. This column is
  label encoded.
  2. tx_name: Name of the developer who attempted the test. This column is label
  encoded.
  3. tx_difficulty: Difficulty of the task
  4. total_correctness: predetermined correctness score given for each task
  5. total_compute: predetermined compute score given for each task
  6. total_robustness: predetermined robustness score given for each task
  7. total_memtotal: predetermined memtotal score given for each task
  8. made_submission: boolean column which determines if developer submitted
  the code or not
  9. compile_success: boolean column which determines if submitted code
  compiled successfully
  10. score_percentage: Score for the task achieved by the developer based on
  successful test cases
  11. Time spent: proportion of total time spent on the task by the developer
  attempting the task. E.g 0.5 would mean a developer spent 15 minutes out of
  30 minutes allowed for the task.
  12. Remarks on Score: remarks on the total score achieved by developer.
  Represents if the developer failed altogether, passed partially or completed
  the task correctly. 0 represents, the developer didn’t compile the code.
  13. id_task_session: unique id for each task session. There are multiple tasks in
  a test attempted by the developer and each task has a unique id.
  14. js_comments: After the task is submitted, some predefined questions are
  asked to the developer. This column contains the answers to those questions
  15. id_infra_instan: id of repository for the task session. A repository is created for
  each task session, in which commits are made automatically every 10s from
  the start to end of the test.
  PA Backend makes automatic commits on behalf of the developer every 10
  seconds. Eg. In a task of 30 minutes, 180 commits would be made on
  developer’s behalf.
    ● The columns ending with “_all” contain the sum of static metrics for all
    commits made at 10 seconds distance.

  16. nu_pgmr_comment_flux_all: Sum of flux in comments length between
  subsequent commits.
  17. nu_pgmr_cyclo_flux_all: Sum of flux in cyclomatic complexity for all commits
  made(at 10 seconds distance). Cyclomatic complexity is the measure of the
  number of linearly independent paths in code. For more info check here .
  18. nu_pgmr_filesize_flux_all: sum of flux in file size for all commits
  19. nu_pgmr_nom_flux_all: sum of flux in number of methods for all commits.
  NOM is defined as the total number of methods in a class, including all public,
  private and protected methods.It indicates the classes that may be trying to
  do too much work themselves; i.e., they provide too much functionality.
  20. nu_pgmr_dac_flux_all: sum of flux in data abstraction coupling for all
  commits.The DAC measures the coupling complexity caused by Abstract
  Data Types (ADTs).
  21. nu_pgmr_fanout_flux_all: sum of fanout flux for all commits. Fan-out is
  defined as the number of local flows from a procedure plus the number of
  data structures that procedure updates.
  22. nu_loc_flux_source_all: sum of flux in number of logical lines of code for all
  commits.
  23. nu_loc_added_source_all: sum of number of lines of source code added by
  the developer for all commits. Eg. if 1 line is added in the first 10 seconds and
  1 line of code is added in the next 10 seconds. Nu_loc_added_source_all
  would be 20.
  24. nu_ce_models_units_all: sum of coding effort of the developer for the task
  based on static metrics. Coding effort is an abstract number which represents
  the effort required to write a piece of code. More the ce, more the effort it will
  take to write that code. The ce units number is further converted to hours for
  better interpretability.
  25. nu_aberrant_ce_units_all: sum of aberrant coding effort of the developer for
  the task based on static metrics. Aberrant coding effort represents the
  percentage of coding effort which is not maintainable. More the ab_ce less
  the code maintainability. The ab_ce is also converted to hours for better
  interpretability.
  26. nu_ce_hours_all: nu_ce_models_units_all converted to hours.
  27. nu_aberrant_ce_all: nu_aberrant_ce_units_all converted to hours
  28. id_test_session: id of the test session attempted by the developer
  PA Backend tracks the last snapshot of code submitted by the developer.
  ● The columns ending with “_submit” contain the static metrics for that
  submitted code against the initial code given to the developer.
  ○ Eg. if the initial code given to the developer had 2 lines of code
  and the submitted code contained 10 lines of code, loc_submit
  would be 8.
  ○ Eg. if the initial code given to the developer had 0 lines of
  code(no code given to start with) and the submitted code
  contained 10 lines of code, loc_submit would be 10.
  29. loc_submit: number of lines of code present in the code submitted by the
  candidate against initial code.
  30. cyclo_submit: cyclomatic complexity of the code at the time of submission against
  initial code.
  31. nom_submit: nom metric for the code at the time of submission against initial
  code
  32. dac_submit: dac metric for the submitted code against initial code
  33. fanout_submit: fanout metric for the submitted code against initial code
  34. ce_units_submit: definition same as 24. Point. Calculated for the submitted code.
  35. aberrant_ce_units_submit: definition same as 25. Calculated for the submitted
  code.
  36. correctness_norm: normalized correctness score achieved by the candidate for
  the task. “norm” represents proportion of correctness out of total correctness
  37. compute_norm: normalized compute score achieved by the candidate for the
  task. “norm” represents proportion of compute out of total compute
  38. robustness_norm: normalized robustness score achieved by the candidate for the
  task. “norm” represents proportion of robustness out of total robustness
  39. memtotal_norm: normalized memtotal score achieved by the candidate for the
  task. “norm” represents proportion of memtotal out of total memtotal
  40. task_score: combined score obtained by the candidate for the task. Calculated
  simply by adding the norm scores and dividing by the sum of total achievable
  scores for correctness,compute,robustness and memtotal.
  41. tx_file_type: file type of the code file written by the developer for the task

# Dependent Variables
  1. BCE/day : Average productivity hours of work put in by the developer per day  
  a. Ranges from 0-5 Hours.  
  b. Calculated on a developer level  
  c. A high bce/day means the developer would be a star performer when
  they get into the organization.

 # Note
    1. The provided training data is aggregated on a task level. There are a total of 330
    tasks.
    2. A test can contain multiple tasks
    3. A developer can attempt multiple tests
    4. BCE/day ranges from 0-5 hours
    
    
