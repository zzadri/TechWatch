# Rate Limiter

## Sources:

-   [Mozilla Developer Network - Rate Limit](https://developer.mozilla.org/en-US/docs/Glossary/Rate_limit)
-   [Cloudflare - WAF Rate Limiting Rules Best Practices](https://developers.cloudflare.com/waf/rate-limiting-rules/best-practices/)

# EN

## Summary:

Rate limiting allows restricting the number of requests a client can make over a
given period. Standard server response: HTTP 429 + Retry-After header.

Cloudflare: five typical use cases — login, scraping, account creation, REST
API, GraphQL API — with examples of thresholds and actions (throttle, challenge,
block). Their "Advanced Rate Limiting" goes beyond simple IP counting: you can
target a cookie, a header, the JA3 fingerprint, etc. Latest additions (threshold
analytics, API v2) simplify CI/CD integration.

## Advice Received:

-   Start broad (limit all API), log, then tighten
-   For specific cases, segment by critical endpoint (/login, /api/\*, etc.)
-   Vary the counting key: IP → public; cookie or API-Key → authenticated routes
-   Build gradually, short blocking then long blocking

## Opinion:

The rate limiter is a more than necessary middleware for projects. It has
crucial importance and adds an extra layer of security to our applications.

## Example:

### Program.cs

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

# FR

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
    options.GlobalLimiter = PartitionedRateLimiter.Create<HttpContext, string>(context =>
    {
        var clientIp = context.Connection.RemoteIpAddress?.ToString() ?? "Unknown";

        if (clientIp == "Unknown")
        {
            options.RejectionStatusCode = 400;
        }

        return RateLimitPartition.GetFixedWindowLimiter(clientIp, partitionOptions =>
        {
            return new FixedWindowRateLimiterOptions
            {
                PermitLimit = int.Parse(builder.Configuration["RateLimiter:PermitLimit"]!),
                Window = TimeSpan.FromMinutes(int.Parse(builder.Configuration["RateLimiter:WaitMinutes"]!)),
                QueueProcessingOrder = QueueProcessingOrder.OldestFirst,
                QueueLimit = int.Parse(builder.Configuration["RateLimiter:QueueLimit"]!)
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
