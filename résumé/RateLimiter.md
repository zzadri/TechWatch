# Rate Limiting

## Source :

-   [Mozilla Developer Network - Rate Limit](https://developer.mozilla.org/en-US/docs/Glossary/Rate_limit)
-   [Cloudflare - WAF Rate Limiting Rules Best Practices](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/)

## Résumé :

Le rate limiting permet de limiter le nombre de requêtes qu'un client peut faire
sur une période donnée. Réponse standard côté serveur : HTTP 429 + header
Retry-After.

Cloudflare : cinq cas d'usage types — login, scraping, création de compte, API
REST, API GraphQL — avec des exemples de seuils et d'actions (throttle,
challenge, block). Leur "Advanced Rate Limiting" va au-delà du simple comptage
IP : on peut viser un cookie, un header, le fingerprint JA3, etc. Derniers
ajouts (analytics de seuils, API v2) simplifient l'intégration CI/CD.

## Conseil reçu :

-   Commencer large (limiter toute api), logguer, puis resserrer
-   Si point spécifique, segmenter par endpoint critique (/login, /api/\*, etc.)
-   Varier la clé de comptage : IP → public ; cookie ou API-Key → routes
    authentifiées
-   Monter crescendo, blocage court puis blocage long

## Avis :

Le rate limiter est un middleware plus que nécessaire sur les projets. Il a une
importance cruciale et permet d'ajouter une couche de sécurité en plus sur nos
applications.

## Exemple :

### Programe.cs

```csharp
using System.Threading.RateLimiting;

builder.Services.AddRateLimiter(options =>
{
    options.GlobalLimiter = PartitionedRateLimiter.CreateHttpContext((string context) =>
    {
        var clientIp = context.Connection.RemoteIpAddress?.ToString() ?? "unknown";

        if (clientIp == "unknown")
        {
            options.RejectionStatusCode = 400;

            return;
        }

        return RateLimitPartition.GetFixedWindowLimiter(clientIp, partition =>
        {
            return new FixedWindowRateLimiterOptions
            {
                PermitLimit = int.Parse(builder.Configuration["RateLimiter:PermitLimit"]),
                Window = TimeSpan.FromMinutes(int.Parse(builder.Configuration["RateLimiter:WaitMinutes"])),
                QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
                QueueLimit = int.Parse(builder.Configuration["RateLimiter:QueueLimit"])
            };
        });
    });

    options.RejectionStatusCode = 429;
});

app.UseRateLimiter();
```

### appsettings.Development.json

```json
{
    "ConnectionStrings": {
        "DefaultConnection": "xxxxxxxxxxxxxxxxxxxxxx"
    },
    "AllowedHosts": "*",
    "Jwt": {
        "Key": "xxxxxxxxxxxxxxxxxxxxxx",
        "Issuer": "",
        "Audience": "",
        "ExpireMinutes": 60
    },
    "RateLimiter": {
        "PermitLimit": 3000,
        "QueueLimit": 0,
        "WaitMinutes": 1
    },
    "ApiVersion": "1.0.0"
}
```
