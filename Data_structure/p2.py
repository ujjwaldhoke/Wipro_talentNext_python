def find_runner_up_score(scores):
    unique_scores = set(scores)
    sorted_scores = sorted(unique_scores, reverse=True)
    if len(sorted_scores) > 1:
        return sorted_scores[1]
    else:
        return None

scores = [2, 3, 6, 6, 5]
runner_up_score = find_runner_up_score(scores)

if runner_up_score is not None:
    print(runner_up_score)