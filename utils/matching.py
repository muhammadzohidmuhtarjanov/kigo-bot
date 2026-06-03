from utils.texts import sport_name, level_name, format_name, times_display

MAX_SCORE = 100


def _score(user_a: dict, user_b: dict, sport: str, sports_b: list) -> int:
    score = 0

    if user_a["city"].lower().strip() == user_b["city"].lower().strip():
        score += 40

    sport_b = next((s for s in sports_b if s["sport"] == sport), None)
    if sport_b:
        if user_a.get("_current_level") == sport_b["level"]:
            score += 30

        fmt_a = user_a.get("_current_format", "any")
        fmt_b = sport_b.get("format", "any")
        if fmt_a == fmt_b or "any" in (fmt_a, fmt_b):
            score += 10

    times_a = set(user_a.get("available_times") or [])
    times_b = set(user_b.get("available_times") or [])
    score += len(times_a & times_b) * 15

    if user_a["age_group"] == user_b["age_group"]:
        score += 5

    return min(score, MAX_SCORE)


def rank_candidates(
    current_user: dict,
    current_sport_record: dict,
    candidates: list,
    lang: str,
) -> list:
    enriched_user = {
        **current_user,
        "_current_level": current_sport_record["level"],
        "_current_format": current_sport_record.get("format", "any"),
    }

    scored = []
    for c in candidates:
        candidate_sports = [
            {"sport": c["us_sport"], "level": c["us_level"], "format": c["us_format"]}
        ]
        sc = _score(enriched_user, c, c["us_sport"], candidate_sports)
        scored.append({
            "id": c["id"],
            "name": c["name"],
            "city": c["city"],
            "age_group": c["age_group"],
            "username": c.get("username"),
            "available_times": c.get("available_times") or [],
            "sport": c["us_sport"],
            "level": c["us_level"],
            "format": c.get("us_format", "any"),
            "rating": c.get("rating", 0),
            "rating_count": c.get("rating_count", 0),
            "score": sc,
            "score_pct": sc,
            "sport_display": sport_name(c["us_sport"], lang),
            "level_display": level_name(c["us_level"], lang),
            "format_display": format_name(c.get("us_format", "any"), lang),
            "times_display": times_display(c.get("available_times") or [], lang),
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored
