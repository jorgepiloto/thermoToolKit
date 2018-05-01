





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-xDUBo/erIsvp+BfhdzOufUdXzU28h21fW2/HU+uLqSKuu06jMMM4JnCtZ3TiRolRoTS3w9q6FQKKPi8Ai5wt+A==" rel="stylesheet" href="https://assets-cdn.github.com/assets/frameworks-482d575624bca06cd70dd916252519ab.css" />
  <link crossorigin="anonymous" media="all" integrity="sha512-Zv3x09u0Axvb3XVv1qb/xBokBjv++6VinZTd9QnYSYDsshwUhTOvqzoFp8Kw8fghtuWEr5Dfe+/TaeUJy5sEJw==" rel="stylesheet" href="https://assets-cdn.github.com/assets/github-98f0e9b94fdbb019dde1c304f706c1a4.css" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>numericalunits/numericalunits.py at master · sbyrnes321/numericalunits</title>
    <meta name="description" content="GitHub is where people build software. More than 27 million people use GitHub to discover, fork, and contribute to over 80 million projects.">
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta property="og:image" content="https://avatars2.githubusercontent.com/u/1857674?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="sbyrnes321/numericalunits" /><meta property="og:url" content="https://github.com/sbyrnes321/numericalunits" /><meta property="og:description" content="numericalunits python package" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjU3NTY0MDE1OjZjZjMxMzBlMzE5ODg1OGY5YWZlMjA5OGZhZjU4MzQ3NjY3YWQ0NTM0ZTIxMWUzOTVhMzFlMTE3MjcyNTUwMGM=--15ff73fba3f2c64170efef2747e1eb548aabcbce">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="C11A:099A:C8607B:167C914:5AE855D2" data-pjax-transient>


  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-request_id" content="C11A:099A:C8607B:167C914:5AE855D2" /><meta name="octolytics-dimension-region_edge" content="iad" /><meta name="octolytics-dimension-region_render" content="iad" /><meta name="octolytics-actor-id" content="28702884" /><meta name="octolytics-actor-login" content="IngenieroDeAviones" /><meta name="octolytics-actor-hash" content="d58f283686448689c9b8e98b6aa259feeb71c1c8f4c1109479f605093c028db9" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="IngenieroDeAviones">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="NzRlNGIyYjk1NzVkNWE2MzNkNzdmMWUxYzI3MmFjNGM2NGFmMGNhNWQ5MzBlNGU1NjBhYTQ5NDczYzE3NmE4Nnx7InJlbW90ZV9hZGRyZXNzIjoiODEuNjEuNjAuMTYxIiwicmVxdWVzdF9pZCI6IkMxMUE6MDk5QTpDODYwN0I6MTY3QzkxNDo1QUU4NTVEMiIsInRpbWVzdGFtcCI6MTUyNTE3NTc2NiwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="UNIVERSE_BANNER,FREE_TRIALS,MARKETPLACE_INSIGHTS,MARKETPLACE_SELF_SERVE,MARKETPLACE_FREE_APPS,MARKETPLACE_INSIGHTS_CONVERSION_PERCENTAGES,MOBILE_COMMENT_ACTIONS">

  <meta name="html-safe-nonce" content="00c7a1e62999e00f5aca5915ea763af30d098b5a">

  <meta http-equiv="x-pjax-version" content="99ce659da08e86e1f8db0a01f11f5fa4">
  

      <link href="https://github.com/sbyrnes321/numericalunits/commits/master.atom" rel="alternate" title="Recent Commits to numericalunits:master" type="application/atom+xml">

  <meta name="description" content="numericalunits python package">
  <meta name="go-import" content="github.com/sbyrnes321/numericalunits git https://github.com/sbyrnes321/numericalunits.git">

  <meta name="octolytics-dimension-user_id" content="1857674" /><meta name="octolytics-dimension-user_login" content="sbyrnes321" /><meta name="octolytics-dimension-repository_id" content="4959631" /><meta name="octolytics-dimension-repository_nwo" content="sbyrnes321/numericalunits" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="4959631" /><meta name="octolytics-dimension-repository_network_root_nwo" content="sbyrnes321/numericalunits" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/sbyrnes321/numericalunits/blob/master/numericalunits.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">


  <meta name="u2f-support" content="true">

<link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex flex-justify-between px-3 container-lg">
    <div class="d-flex flex-justify-between ">
      <div class="">
        <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg height="32" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>

      </div>

    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" data-scope-type="Repository" data-scope-id="4959631" data-scoped-search-url="/sbyrnes321/numericalunits/search" data-unscoped-search-url="/search" action="/sbyrnes321/numericalunits/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
    <label class="form-control header-search-wrapper  js-chromeless-input-container">
          <a class="header-search-scope no-underline" href="/sbyrnes321/numericalunits/blob/master/numericalunits.py">This repository</a>
      <input type="text"
        class="form-control header-search-input  js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s,/"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off"
        >
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
                Pull requests
</a>            </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
                Issues
</a>            </li>
                <li>
                  <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar, group:" data-selected-links=" /marketplace" href="/marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      
    <a aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s  js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:read" data-channel="notification-changed:28702884" href="/notifications">
        <span class="mail-status "></span>
        <svg class="octicon octicon-bell" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"/></svg>
</a>
    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg class="octicon octicon-plus float-left mr-1 mt-1" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="sbyrnes321/numericalunits">This repository</span>
  </div>
    <a class="dropdown-item" href="/sbyrnes321/numericalunits/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@IngenieroDeAviones" class="avatar float-left mr-1" src="https://avatars1.githubusercontent.com/u/28702884?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">IngenieroDeAviones</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/IngenieroDeAviones" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/IngenieroDeAviones?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="/29R/gt7oL5OpjDgcR2DTI6vB2gvV0NFIuWfzRbgTwS0xTNIx+sJWLgNXcA0P4dpScibN6e4lcSeyZpx5xZyjA==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>



        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="sr-only right-0" action="/logout" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="bVRe6NU3Xr+tt0U/axBPv95iwHlTB+zjK8GTVrPODKMm/jxeGaf3WVscKB8uMkuaGQVcJtvoOmKX7ZbqQjgxKw==" />
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      







  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-autosubmit="true" data-remote="true" class="js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="GkpchJjgqtscAy8Zkj/kwfxD+mEwK2+LM5zeY5BuIP/k7sfQ1SxwizkmdeibXvFUHLjA6DvfviJy1qDcQ1u81Q==" />      <input type="hidden" name="repository_id" id="repository_id" value="4959631" class="form-control" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/sbyrnes321/numericalunits/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/sbyrnes321/numericalunits/watchers"
            aria-label="7 users are watching this repository">
            7
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_included" value="included" checked="checked" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_subscribed" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-eye" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input type="radio" name="do" id="do_ignore" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg class="octicon octicon-mute" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="starred js-social-form" action="/sbyrnes321/numericalunits/unstar" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="nT418gh7HH6V2FBOsEh7LytGes0RbjiV42DapLtxyAQeWGngAHfNYK/2G8vlSk5hCyddOQwFYHtD7GXmPkc4iA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar sbyrnes321/numericalunits"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/sbyrnes321/numericalunits/stargazers"
           aria-label="46 users starred this repository">
          46
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="unstarred js-social-form" action="/sbyrnes321/numericalunits/star" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="pwaB7tfdQhv9tdSIz0vs+UUwbNVpDy2+cVvXvsWFPsBc6Oq4taLEtG9OaurSFIaYh513nnHB8il1RkSceBJvcw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star sbyrnes321/numericalunits"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg class="octicon octicon-star" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/sbyrnes321/numericalunits/stargazers"
           aria-label="46 users starred this repository">
          46
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/sbyrnes321/numericalunits/fork" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="IlyV8u+1Y5Fqyhf7S9u8e77FdoLXi9Gl4qomhYwTyGwPWjycefzSOKnGrlQ/HyvAUtA9cdESelIpySMYTV+SGw==" />
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of sbyrnes321/numericalunits to your account"
                aria-label="Fork your own copy of sbyrnes321/numericalunits to your account">
              <svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
              Fork
            </button>
</form>
    <a href="/sbyrnes321/numericalunits/network" class="social-count"
       aria-label="13 users forked this repository">
      13
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a class="url fn" rel="author" href="/sbyrnes321">sbyrnes321</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a data-pjax="#js-repo-pjax-container" href="/sbyrnes321/numericalunits">numericalunits</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /sbyrnes321/numericalunits" href="/sbyrnes321/numericalunits">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /sbyrnes321/numericalunits/issues" href="/sbyrnes321/numericalunits/issues">
        <svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a data-hotkey="g p" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /sbyrnes321/numericalunits/pulls" href="/sbyrnes321/numericalunits/pulls">
      <svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /sbyrnes321/numericalunits/projects" href="/sbyrnes321/numericalunits/projects">
      <svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /sbyrnes321/numericalunits/wiki" href="/sbyrnes321/numericalunits/wiki">
      <svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /sbyrnes321/numericalunits/pulse" href="/sbyrnes321/numericalunits/pulse">
    <svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/sbyrnes321/numericalunits/blob/ab608390f07102857b66ebb82e47ea426b5aec77/numericalunits.py">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:ea820a65ae323395a19c5cfc160a2118 -->

  <div class="file-navigation">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg class="octicon octicon-x js-menu-close" role="img" aria-label="Close" viewBox="0 0 12 16" version="1.1" width="12" height="16"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/sbyrnes321/numericalunits/blob/master/numericalunits.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/sbyrnes321/numericalunits/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <clipboard-copy for="blob-path" class="btn btn-sm BtnGroup-item">
        Copy path
      </clipboard-copy>
    </div>
    <div id="blob-path" class="breadcrumb">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a data-pjax="true" href="/sbyrnes321/numericalunits"><span>numericalunits</span></a></span></span><span class="separator">/</span><strong class="final-path">numericalunits.py</strong>
    </div>
  </div>


  <include-fragment src="/sbyrnes321/numericalunits/contributors/master/numericalunits.py" class="commit-tease">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>


  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/sbyrnes321/numericalunits/raw/master/numericalunits.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/sbyrnes321/numericalunits/blame/master/numericalunits.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/sbyrnes321/numericalunits/commits/master/numericalunits.py">History</a>
    </div>


          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/sbyrnes321/numericalunits/edit/master/numericalunits.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="MV4+p5lRL3oLiLGayKO+SxefnvNiawUDivDHd4ZFvVPLSVNi7IIJM45P8ANS1X595cODvfHMBb3nYs67KFdy5Q==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/sbyrnes321/numericalunits/delete/master/numericalunits.py" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="CWAGFLSkr8MjOfjCEd8B1oahNBNz8V6tK1nmbpj41Nse3+jBzn8DoAwAMQb3atrkoaoW/pEz0NR7ceMkVsfqNg==" />
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      414 lines (372 sloc)
      <span class="file-info-divider"></span>
    13.7 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-s">For information and usage see README, or http://pypi.python.org/pypi/numericalunits</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Copyright (C) 2012-2017 Steven Byrnes</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> division</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> math <span class="pl-k">import</span> pi</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">__version__</span> <span class="pl-k">=</span> <span class="pl-c1">1.21</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>######### Set all variables, to help introspection libraries ################</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> This part is functionally pointless, it only helps IDE autocompletion</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> / introspection libraries know that these variables exist. The actual</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> values are set below, using the &quot;global&quot; keyword inside functions.</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">m <span class="pl-k">=</span> kg <span class="pl-k">=</span> s <span class="pl-k">=</span> C <span class="pl-k">=</span> K <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">cm <span class="pl-k">=</span> mm <span class="pl-k">=</span> um <span class="pl-k">=</span> nm <span class="pl-k">=</span> pm <span class="pl-k">=</span> fm <span class="pl-k">=</span> km <span class="pl-k">=</span> angstrom <span class="pl-k">=</span> lightyear <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">    astro_unit <span class="pl-k">=</span> pc <span class="pl-k">=</span> kpc <span class="pl-k">=</span> Mpc <span class="pl-k">=</span> Gpc <span class="pl-k">=</span> inch <span class="pl-k">=</span> foot <span class="pl-k">=</span> mile <span class="pl-k">=</span> thou <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">L <span class="pl-k">=</span> mL <span class="pl-k">=</span> uL <span class="pl-k">=</span> nL <span class="pl-k">=</span> pL <span class="pl-k">=</span> fL <span class="pl-k">=</span> aL <span class="pl-k">=</span> kL <span class="pl-k">=</span> <span class="pl-c1">ML</span> <span class="pl-k">=</span> <span class="pl-c1">GL</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">ms <span class="pl-k">=</span> us <span class="pl-k">=</span> ns <span class="pl-k">=</span> ps <span class="pl-k">=</span> fs <span class="pl-k">=</span> minute <span class="pl-k">=</span> hour <span class="pl-k">=</span> day <span class="pl-k">=</span> week <span class="pl-k">=</span> year <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">Hz <span class="pl-k">=</span> mHz <span class="pl-k">=</span> kHz <span class="pl-k">=</span> MHz <span class="pl-k">=</span> GHz <span class="pl-k">=</span> THz <span class="pl-k">=</span> PHz <span class="pl-k">=</span> rtHz <span class="pl-k">=</span> rpm <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">g <span class="pl-k">=</span> mg <span class="pl-k">=</span> ug <span class="pl-k">=</span> ng <span class="pl-k">=</span> pg <span class="pl-k">=</span> fg <span class="pl-k">=</span> tonne <span class="pl-k">=</span> amu <span class="pl-k">=</span> Da <span class="pl-k">=</span> kDa <span class="pl-k">=</span> lbm <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">J <span class="pl-k">=</span> mJ <span class="pl-k">=</span> uJ <span class="pl-k">=</span> nJ <span class="pl-k">=</span> pJ <span class="pl-k">=</span> fJ <span class="pl-k">=</span> kJ <span class="pl-k">=</span> <span class="pl-c1">MJ</span> <span class="pl-k">=</span> <span class="pl-c1">GJ</span> <span class="pl-k">=</span> erg <span class="pl-k">=</span> eV <span class="pl-k">=</span> meV <span class="pl-k">=</span> keV <span class="pl-k">=</span> MeV <span class="pl-k">=</span> GeV <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    TeV <span class="pl-k">=</span> btu <span class="pl-k">=</span> smallcal <span class="pl-k">=</span> kcal <span class="pl-k">=</span> Wh <span class="pl-k">=</span> kWh <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">NA</span> <span class="pl-k">=</span> mol <span class="pl-k">=</span> mmol <span class="pl-k">=</span> umol <span class="pl-k">=</span> nmol <span class="pl-k">=</span> pmol <span class="pl-k">=</span> fmol <span class="pl-k">=</span> M <span class="pl-k">=</span> mM <span class="pl-k">=</span> uM <span class="pl-k">=</span> nM <span class="pl-k">=</span> pM <span class="pl-k">=</span> fM <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">N <span class="pl-k">=</span> mN <span class="pl-k">=</span> uN <span class="pl-k">=</span> nN <span class="pl-k">=</span> pN <span class="pl-k">=</span> fN <span class="pl-k">=</span> kN <span class="pl-k">=</span> <span class="pl-c1">MN</span> <span class="pl-k">=</span> <span class="pl-c1">GN</span> <span class="pl-k">=</span> dyn <span class="pl-k">=</span> lbf <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">Pa <span class="pl-k">=</span> hPa <span class="pl-k">=</span> kPa <span class="pl-k">=</span> MPa <span class="pl-k">=</span> GPa <span class="pl-k">=</span> bar <span class="pl-k">=</span> mbar <span class="pl-k">=</span> cbar <span class="pl-k">=</span> dbar <span class="pl-k">=</span> kbar <span class="pl-k">=</span> Mbar <span class="pl-k">=</span> atm <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    torr <span class="pl-k">=</span> mtorr <span class="pl-k">=</span> psi <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">W <span class="pl-k">=</span> mW <span class="pl-k">=</span> uW <span class="pl-k">=</span> nW <span class="pl-k">=</span> pW <span class="pl-k">=</span> kW <span class="pl-k">=</span> <span class="pl-c1">MW</span> <span class="pl-k">=</span> <span class="pl-c1">GW</span> <span class="pl-k">=</span> <span class="pl-c1">TW</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">degFinterval <span class="pl-k">=</span> degCinterval <span class="pl-k">=</span> mK <span class="pl-k">=</span> uK <span class="pl-k">=</span> nK <span class="pl-k">=</span> pK <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">mC <span class="pl-k">=</span> uC <span class="pl-k">=</span> nC <span class="pl-k">=</span> Ah <span class="pl-k">=</span> mAh <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">A <span class="pl-k">=</span> mA <span class="pl-k">=</span> uA <span class="pl-k">=</span> nA <span class="pl-k">=</span> pA <span class="pl-k">=</span> fA <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">V <span class="pl-k">=</span> mV <span class="pl-k">=</span> uV <span class="pl-k">=</span> nV <span class="pl-k">=</span> kV <span class="pl-k">=</span> <span class="pl-c1">MV</span> <span class="pl-k">=</span> <span class="pl-c1">GV</span> <span class="pl-k">=</span> <span class="pl-c1">TV</span> <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">ohm <span class="pl-k">=</span> mohm <span class="pl-k">=</span> kohm <span class="pl-k">=</span> Mohm <span class="pl-k">=</span> Gohm <span class="pl-k">=</span> S <span class="pl-k">=</span> mS <span class="pl-k">=</span> uS <span class="pl-k">=</span> nS <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">T <span class="pl-k">=</span> mT <span class="pl-k">=</span> uT <span class="pl-k">=</span> nT <span class="pl-k">=</span> G <span class="pl-k">=</span> mG <span class="pl-k">=</span> uG <span class="pl-k">=</span> kG <span class="pl-k">=</span> Oe <span class="pl-k">=</span> Wb <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">F <span class="pl-k">=</span> uF <span class="pl-k">=</span> nF <span class="pl-k">=</span> pF <span class="pl-k">=</span> fF <span class="pl-k">=</span> aF <span class="pl-k">=</span> H <span class="pl-k">=</span> mH <span class="pl-k">=</span> uH <span class="pl-k">=</span> nH <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">c0 <span class="pl-k">=</span> mu0 <span class="pl-k">=</span> eps0 <span class="pl-k">=</span> Z0 <span class="pl-k">=</span> hPlanck <span class="pl-k">=</span> hbar <span class="pl-k">=</span> kB <span class="pl-k">=</span> GNewton <span class="pl-k">=</span> sigmaSB <span class="pl-k">=</span> alphaFS <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">Rgas <span class="pl-k">=</span> e <span class="pl-k">=</span> uBohr <span class="pl-k">=</span> uNuc <span class="pl-k">=</span> aBohr <span class="pl-k">=</span> me <span class="pl-k">=</span> mp <span class="pl-k">=</span> mn <span class="pl-k">=</span> Rinf <span class="pl-k">=</span> Ry <span class="pl-k">=</span> Hartree <span class="pl-k">=</span> \</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">    ARichardson <span class="pl-k">=</span> Phi0 <span class="pl-k">=</span> KJos <span class="pl-k">=</span> RKlitz <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">REarth <span class="pl-k">=</span> g0 <span class="pl-k">=</span> Msolar <span class="pl-k">=</span> MEarth <span class="pl-k">=</span> <span class="pl-c1">0</span>.</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>########################## Main code #######################################</span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">reset_units</span>(<span class="pl-smi">seed</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Set all units to new, self-consistent, floating-point values. See package</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    documentation for detailed explanation and examples:</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    http://pypi.python.org/pypi/numericalunits</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    reset_units() --&gt; units are randomized. This is the suggested use. Run this</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    before your calculation, display the final answer, then re-run this, then</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    re-disply the final answer. If you get the same answers both times, then</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    your calculations are almost guaranteed to be free of</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    dimensional-analysis-violating errors. reset_units() is run automatically</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    the first time this module is imported.</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    reset_units(&#39;SI&#39;) --&gt; Set units so that all values are given in standard SI</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    units (meters-kilograms-seconds) by default. In this mode, there is no way</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    to test for dimensional-analysis-violating errors.</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    reset_units(x) --&gt; If you pass any other argument x, it&#39;s used as the seed</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    for the random number generator.</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> random</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> m, kg, s, C, K</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> seed <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>SI<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> <span class="pl-c1">1</span>.</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        kg <span class="pl-k">=</span> <span class="pl-c1">1</span>.</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        s <span class="pl-k">=</span> <span class="pl-c1">1</span>.</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">        C <span class="pl-k">=</span> <span class="pl-c1">1</span>.</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        K <span class="pl-k">=</span> <span class="pl-c1">1</span>.</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">        prior_random_state <span class="pl-k">=</span> random.getstate()</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> seed <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">            random.seed()</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">            random.seed(seed)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> <span class="pl-c1">10</span>. <span class="pl-k">**</span> random.uniform(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>) <span class="pl-c"><span class="pl-c">#</span>meter</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        kg <span class="pl-k">=</span> <span class="pl-c1">10</span>. <span class="pl-k">**</span> random.uniform(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>) <span class="pl-c"><span class="pl-c">#</span>kilogram</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        s <span class="pl-k">=</span> <span class="pl-c1">10</span>. <span class="pl-k">**</span> random.uniform(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>) <span class="pl-c"><span class="pl-c">#</span>second</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        C <span class="pl-k">=</span> <span class="pl-c1">10</span>. <span class="pl-k">**</span> random.uniform(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>) <span class="pl-c"><span class="pl-c">#</span> coulombs</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        K <span class="pl-k">=</span> <span class="pl-c1">10</span>. <span class="pl-k">**</span> random.uniform(<span class="pl-k">-</span><span class="pl-c1">1</span>,<span class="pl-c1">1</span>) <span class="pl-c"><span class="pl-c">#</span> kelvins</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Leave the random generator like I found it, in case something else is</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> using it.</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        random.setstate(prior_random_state)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">    set_derived_units_and_constants()</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">set_derived_units_and_constants</span>():</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Assuming that the base units (m, kg, s, C, K) have already been set as</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    floating-point values, this function sets all other units and constants</span></td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    to the appropriate, self-consistent values.</span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Length</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> cm, mm, um, nm, pm, fm, km, angstrom, lightyear, \</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        astro_unit, pc, kpc, Mpc, Gpc, inch, foot, mile, thou</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">    cm <span class="pl-k">=</span> <span class="pl-c1">1e-2</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">    mm <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    um <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">    nm <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    pm <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">    fm <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">    km <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">    angstrom <span class="pl-k">=</span> <span class="pl-c1">1e-10</span> <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>Å<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> angstrom <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">    lightyear <span class="pl-k">=</span> <span class="pl-c1">9460730472580800</span>. <span class="pl-k">*</span> m</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    astro_unit <span class="pl-k">=</span> <span class="pl-c1">149597870700</span>. <span class="pl-k">*</span> m <span class="pl-c"><span class="pl-c">#</span>astronomical unit</span></td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    pc <span class="pl-k">=</span> (<span class="pl-c1">648000</span>.<span class="pl-k">/</span>pi) <span class="pl-k">*</span> astro_unit <span class="pl-c"><span class="pl-c">#</span>parsec</span></td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">    kpc <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> pc</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">    Mpc <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> pc</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    Gpc <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> pc</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">    inch <span class="pl-k">=</span> <span class="pl-c1">2.54</span> <span class="pl-k">*</span> cm</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">    foot <span class="pl-k">=</span> <span class="pl-c1">12</span>. <span class="pl-k">*</span> inch</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">    mile <span class="pl-k">=</span> <span class="pl-c1">5280</span>. <span class="pl-k">*</span> foot</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">    thou <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> inch  <span class="pl-c"><span class="pl-c">#</span>thousandth of an inch; also called mil</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Volume</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> L, mL, uL, nL, pL, fL, aL, kL, <span class="pl-c1">ML</span>, <span class="pl-c1">GL</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    L <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> m<span class="pl-k">**</span><span class="pl-c1">3</span> <span class="pl-c"><span class="pl-c">#</span>liter</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">    mL <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">    uL <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">    nL <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">    pL <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    fL <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">    aL <span class="pl-k">=</span> <span class="pl-c1">1e-18</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">    kL <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">ML</span> <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GL</span> <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> L</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Time</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> ms, us, ns, ps, fs, minute, hour, day, week, year</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">    ms <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">    us <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">    ns <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">    ps <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">    fs <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">    minute <span class="pl-k">=</span> <span class="pl-c1">60</span>. <span class="pl-k">*</span> s</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">    hour <span class="pl-k">=</span> <span class="pl-c1">60</span>. <span class="pl-k">*</span> minute</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">    day <span class="pl-k">=</span> <span class="pl-c1">24</span>. <span class="pl-k">*</span> hour <span class="pl-c"><span class="pl-c">#</span>solar day</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">    week <span class="pl-k">=</span> <span class="pl-c1">7</span>. <span class="pl-k">*</span> day</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">    year <span class="pl-k">=</span> <span class="pl-c1">365.256363004</span> <span class="pl-k">*</span> day <span class="pl-c"><span class="pl-c">#</span>sidereal year</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Frequency</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> Hz, mHz, kHz, MHz, GHz, THz, PHz, rtHz, rpm</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">    Hz <span class="pl-k">=</span> <span class="pl-c1">1</span>.<span class="pl-k">/</span>s</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">    mHz <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">    kHz <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">    MHz <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">    GHz <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">    THz <span class="pl-k">=</span> <span class="pl-c1">1e12</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">    PHz <span class="pl-k">=</span> <span class="pl-c1">1e15</span> <span class="pl-k">*</span> Hz</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">    rtHz <span class="pl-k">=</span> Hz<span class="pl-k">**</span><span class="pl-c1">0.5</span> <span class="pl-c"><span class="pl-c">#</span> &quot;root Hertz&quot;</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">    rpm <span class="pl-k">=</span> <span class="pl-c1">1</span><span class="pl-k">/</span>minute <span class="pl-c"><span class="pl-c">#</span> revolutions per minute</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">    </td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Angular frequency units</span></td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Example: ω = 3 * kHz·2π means that ω is the angular frequency</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>   corresponding to a rotation whose *ordinary* frequency is 3 kHz.</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Note: These only work in Python 3.</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>Hz·2π<span class="pl-pds">&#39;</span></span>]  <span class="pl-k">=</span>  Hz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>mHz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> mHz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>kHz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> kHz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>MHz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> MHz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>GHz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> GHz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>THz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> THz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>PHz·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> PHz <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>rpm·2π<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> rpm <span class="pl-k">*</span> <span class="pl-c1">2</span><span class="pl-k">*</span>pi</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Mass</span></td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> g, mg, ug, ng, pg, fg, tonne, amu, Da, kDa, lbm</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">    g <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> kg</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    mg <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> g</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">    ug <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> g</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">    ng <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> g</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">    pg <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> g</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">    fg <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> g</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">    tonne <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> kg</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">    amu <span class="pl-k">=</span> <span class="pl-c1">1.660538921e-27</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span>atomic mass unit</span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">    Da <span class="pl-k">=</span> amu <span class="pl-c"><span class="pl-c">#</span>Dalton</span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">    kDa <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> Da</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">    lbm <span class="pl-k">=</span> <span class="pl-c1">0.45359237</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span> pound mass (international avoirdupois pound)</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Energy</span></td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> J, mJ, uJ, nJ, pJ, fJ, kJ, <span class="pl-c1">MJ</span>, <span class="pl-c1">GJ</span>, erg, eV, meV, keV, MeV, GeV, \</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">           TeV, btu, smallcal, kcal, Wh, kWh</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">    J <span class="pl-k">=</span> (kg <span class="pl-k">*</span> m<span class="pl-k">**</span><span class="pl-c1">2</span>)<span class="pl-k">/</span>s<span class="pl-k">**</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">    mJ <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">    uJ <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">    nJ <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">    pJ <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">    fJ <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">    kJ <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">MJ</span> <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GJ</span> <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">    erg <span class="pl-k">=</span> <span class="pl-c1">1e-7</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">    eV <span class="pl-k">=</span> <span class="pl-c1">1.602176565e-19</span> <span class="pl-k">*</span> J</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">    meV <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> eV</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">    keV <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> eV</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">    MeV <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> eV</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">    GeV <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> eV</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">    TeV <span class="pl-k">=</span> <span class="pl-c1">1e12</span> <span class="pl-k">*</span> eV</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">    btu <span class="pl-k">=</span> <span class="pl-c1">1055.056</span> <span class="pl-k">*</span> J  <span class="pl-c"><span class="pl-c">#</span>British thermal unit</span></td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line">    smallcal <span class="pl-k">=</span> <span class="pl-c1">4.184</span> <span class="pl-k">*</span> J <span class="pl-c"><span class="pl-c">#</span>small calorie (&quot;gram calorie&quot;)</span></td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">    kcal <span class="pl-k">=</span> <span class="pl-c1">4184</span>. <span class="pl-k">*</span> J  <span class="pl-c"><span class="pl-c">#</span>kilocalorie (&quot;large Calorie&quot;, &quot;dietary Calorie&quot;)</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">    Wh <span class="pl-k">=</span> <span class="pl-c1">3600</span>. <span class="pl-k">*</span> J <span class="pl-c"><span class="pl-c">#</span>watt-hour</span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">    kWh <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> Wh <span class="pl-c"><span class="pl-c">#</span> kilowatt-hour</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Moles, concentration / molarity</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> <span class="pl-c1">NA</span>, mol, mmol, umol, nmol, pmol, fmol, M, mM, uM, nM, pM, fM</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">NA</span> <span class="pl-k">=</span> <span class="pl-c1">6.02214129e23</span>  <span class="pl-c"><span class="pl-c">#</span>Avogadro&#39;s number</span></td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">    mol <span class="pl-k">=</span> <span class="pl-c1">NA</span>  <span class="pl-c"><span class="pl-c">#</span>1 mole (see README)</span></td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">    mmol <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> mol</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">    umol <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> mol</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">    nmol <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> mol</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">    pmol <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> mol</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">    fmol <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> mol</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">    M <span class="pl-k">=</span> mol<span class="pl-k">/</span>L <span class="pl-c"><span class="pl-c">#</span> molar</span></td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">    mM <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> M</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">    uM <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> M</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    nM <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> M</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">    pM <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> M</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">    fM <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> M</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Force</span></td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> N, mN, uN, nN, pN, fN, kN, <span class="pl-c1">MN</span>, <span class="pl-c1">GN</span>, dyn, lbf</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">    N <span class="pl-k">=</span> (kg <span class="pl-k">*</span> m)<span class="pl-k">/</span>s<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span>newton</span></td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">    mN <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">    uN <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">    nN <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">    pN <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">    fN <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">    kN <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">MN</span> <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GN</span> <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> N</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">    dyn <span class="pl-k">=</span> <span class="pl-c1">1e-5</span> <span class="pl-k">*</span> N <span class="pl-c"><span class="pl-c">#</span>dyne</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">    lbf <span class="pl-k">=</span> <span class="pl-c1">4.4482216152605</span> <span class="pl-k">*</span> N <span class="pl-c"><span class="pl-c">#</span>pound-force (international avoirdupois pound)</span></td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Pressure</span></td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> Pa, hPa, kPa, MPa, GPa, bar, mbar, cbar, dbar, kbar, Mbar, atm, \</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">           torr, mtorr, psi</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    Pa <span class="pl-k">=</span> N<span class="pl-k">/</span>m<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span>pascal</span></td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">    hPa <span class="pl-k">=</span> <span class="pl-c1">1e2</span> <span class="pl-k">*</span> Pa <span class="pl-c"><span class="pl-c">#</span>hectopascal</span></td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">    kPa <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> Pa</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">    MPa <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> Pa</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">    GPa <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> Pa</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    bar <span class="pl-k">=</span> <span class="pl-c1">1e5</span> <span class="pl-k">*</span> Pa</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">    mbar <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> bar</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">    cbar <span class="pl-k">=</span> <span class="pl-c1">1e-2</span> <span class="pl-k">*</span> bar <span class="pl-c"><span class="pl-c">#</span>centibar</span></td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">    dbar <span class="pl-k">=</span> <span class="pl-c1">0.1</span> <span class="pl-k">*</span> bar <span class="pl-c"><span class="pl-c">#</span>decibar</span></td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">    kbar <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> bar</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">    Mbar <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> bar</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">    atm <span class="pl-k">=</span> <span class="pl-c1">101325</span>. <span class="pl-k">*</span> Pa</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">    torr <span class="pl-k">=</span> (<span class="pl-c1">1</span>.<span class="pl-k">/</span><span class="pl-c1">760</span>.) <span class="pl-k">*</span> atm</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">    mtorr <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> torr</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">    psi <span class="pl-k">=</span> lbf <span class="pl-k">/</span> inch<span class="pl-k">**</span><span class="pl-c1">2</span></td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Power</span></td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> W, mW, uW, nW, pW, kW, <span class="pl-c1">MW</span>, <span class="pl-c1">GW</span>, <span class="pl-c1">TW</span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">    W <span class="pl-k">=</span> J<span class="pl-k">/</span>s</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">    mW <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">    uW <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">    nW <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">    pW <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">    kW <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">MW</span> <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GW</span> <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">TW</span> <span class="pl-k">=</span> <span class="pl-c1">1e12</span> <span class="pl-k">*</span> W</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Temperature</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> degFinterval, degCinterval, mK, uK, nK, pK</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">    degFinterval <span class="pl-k">=</span> (<span class="pl-c1">5</span>.<span class="pl-k">/</span><span class="pl-c1">9</span>.) <span class="pl-k">*</span> K <span class="pl-c"><span class="pl-c">#</span> A temperature difference in degrees Fahrenheit</span></td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">    degCinterval <span class="pl-k">=</span> K <span class="pl-c"><span class="pl-c">#</span> A temperature difference in degrees Celsius</span></td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">    mK <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> K</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">    uK <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> K</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">    nK <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> K</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">    pK <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> K</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Charge</span></td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> mC, uC, nC, Ah, mAh</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">    mC <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> C</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">    uC <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> C</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">    nC <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> C</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">    Ah <span class="pl-k">=</span> <span class="pl-c1">3600</span>. <span class="pl-k">*</span> C <span class="pl-c"><span class="pl-c">#</span>amp-hour</span></td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">    mAh <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> Ah</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Current</span></td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> A, mA, uA, nA, pA, fA</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">    A <span class="pl-k">=</span> C<span class="pl-k">/</span>s</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">    mA <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> A</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">    uA <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> A</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">    nA <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> A</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">    pA <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> A</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">    fA <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> A</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Voltage</span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> V, mV, uV, nV, kV, <span class="pl-c1">MV</span>, <span class="pl-c1">GV</span>, <span class="pl-c1">TV</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">    V <span class="pl-k">=</span> J<span class="pl-k">/</span>C</td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">    mV <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">    uV <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">    nV <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">    kV <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">MV</span> <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">GV</span> <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">TV</span> <span class="pl-k">=</span> <span class="pl-c1">1e12</span> <span class="pl-k">*</span> V</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Resistance and conductivity</span></td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> ohm, mohm, kohm, Mohm, Gohm, S, mS, uS, nS</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">    ohm <span class="pl-k">=</span> V <span class="pl-k">/</span> A</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">    mohm <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> ohm</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">    kohm <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> ohm</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">    Mohm <span class="pl-k">=</span> <span class="pl-c1">1e6</span> <span class="pl-k">*</span> ohm</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">    Gohm <span class="pl-k">=</span> <span class="pl-c1">1e9</span> <span class="pl-k">*</span> ohm</td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>Ω<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> ohm <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>mΩ<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> mohm <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>kΩ<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> kohm <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>MΩ<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> Mohm <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>GΩ<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> Gohm <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">    S <span class="pl-k">=</span> <span class="pl-c1">1</span>.<span class="pl-k">/</span>ohm <span class="pl-c"><span class="pl-c">#</span>siemens</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">    mS <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> S</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">    uS <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> S</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">    nS <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> S</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Magnetic fields and fluxes</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> T, mT, uT, nT, G, mG, uG, kG, Oe, Wb</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">    T <span class="pl-k">=</span> (V <span class="pl-k">*</span> s) <span class="pl-k">/</span> m<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span>tesla</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">    mT <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> T</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">    uT <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> T</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">    nT <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> T</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">    G <span class="pl-k">=</span> <span class="pl-c1">1e-4</span> <span class="pl-k">*</span> T <span class="pl-c"><span class="pl-c">#</span>gauss</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">    mG <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> G</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">    uG <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> G</td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">    kG <span class="pl-k">=</span> <span class="pl-c1">1e3</span> <span class="pl-k">*</span> G</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line">    Oe <span class="pl-k">=</span> (<span class="pl-c1">1000</span>.<span class="pl-k">/</span>(<span class="pl-c1">4</span>.<span class="pl-k">*</span>pi)) <span class="pl-k">*</span> A<span class="pl-k">/</span>m <span class="pl-c"><span class="pl-c">#</span>oersted</span></td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">    Wb <span class="pl-k">=</span> J<span class="pl-k">/</span>A <span class="pl-c"><span class="pl-c">#</span>weber</span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Capacitance and inductance</span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> F, uF, nF, pF, fF, aF, H, mH, uH, nH</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">    F <span class="pl-k">=</span> C <span class="pl-k">/</span> V <span class="pl-c"><span class="pl-c">#</span>farad</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">    uF <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> F</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">    nF <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> F</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">    pF <span class="pl-k">=</span> <span class="pl-c1">1e-12</span> <span class="pl-k">*</span> F</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">    fF <span class="pl-k">=</span> <span class="pl-c1">1e-15</span> <span class="pl-k">*</span> F</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">    aF <span class="pl-k">=</span> <span class="pl-c1">1e-18</span> <span class="pl-k">*</span> F</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">    H <span class="pl-k">=</span> m<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-k">*</span> kg <span class="pl-k">/</span> C<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span>henry</span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">    mH <span class="pl-k">=</span> <span class="pl-c1">1e-3</span> <span class="pl-k">*</span> H</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">    uH <span class="pl-k">=</span> <span class="pl-c1">1e-6</span> <span class="pl-k">*</span> H</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">    nH <span class="pl-k">=</span> <span class="pl-c1">1e-9</span> <span class="pl-k">*</span> H</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>Constants--general</span></td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> c0, mu0, eps0, Z0, hPlanck, hbar, kB, GNewton, sigmaSB, alphaFS</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">    c0 <span class="pl-k">=</span> <span class="pl-c1">299792458</span>. <span class="pl-k">*</span> m<span class="pl-k">/</span>s  <span class="pl-c"><span class="pl-c">#</span>speed of light in vacuum</span></td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">    mu0 <span class="pl-k">=</span> <span class="pl-c1">4</span>. <span class="pl-k">*</span> pi <span class="pl-k">*</span> <span class="pl-c1">1e-7</span> <span class="pl-k">*</span> N<span class="pl-k">/</span>A<span class="pl-k">**</span><span class="pl-c1">2</span>  <span class="pl-c"><span class="pl-c">#</span>magnetic constant, permeability of vacuum</span></td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>μ0<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> mu0 <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">    eps0 <span class="pl-k">=</span> <span class="pl-c1">1</span>.<span class="pl-k">/</span>(mu0 <span class="pl-k">*</span> c0<span class="pl-k">**</span><span class="pl-c1">2</span>) <span class="pl-c"><span class="pl-c">#</span>electric constant, permittivity of vacuum</span></td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>ε0<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> eps0 <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">    Z0 <span class="pl-k">=</span> mu0 <span class="pl-k">*</span> c0  <span class="pl-c"><span class="pl-c">#</span>vacuum impedance, 377 ohms</span></td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">    hPlanck <span class="pl-k">=</span> <span class="pl-c1">6.62606957e-34</span> <span class="pl-k">*</span> J<span class="pl-k">*</span>s  <span class="pl-c"><span class="pl-c">#</span>planck constant</span></td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">    hbar <span class="pl-k">=</span> hPlanck <span class="pl-k">/</span> (<span class="pl-c1">2</span>.<span class="pl-k">*</span>pi)  <span class="pl-c"><span class="pl-c">#</span>reduced planck constant</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>ħ<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hbar <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">    kB <span class="pl-k">=</span> <span class="pl-c1">1.3806488e-23</span> <span class="pl-k">*</span> J<span class="pl-k">/</span>K  <span class="pl-c"><span class="pl-c">#</span>Boltzmann constant</span></td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">    GNewton <span class="pl-k">=</span> <span class="pl-c1">6.67384e-11</span> <span class="pl-k">*</span> m<span class="pl-k">**</span><span class="pl-c1">3</span> <span class="pl-k">/</span> (kg <span class="pl-k">*</span> s<span class="pl-k">**</span><span class="pl-c1">2</span>) <span class="pl-c"><span class="pl-c">#</span>Gravitational constant</span></td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">    sigmaSB <span class="pl-k">=</span> <span class="pl-c1">5.670373e-8</span> <span class="pl-k">*</span> W <span class="pl-k">/</span> (m<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-k">*</span> K<span class="pl-k">**</span><span class="pl-c1">4</span>)  <span class="pl-c"><span class="pl-c">#</span>Stefan-Boltzmann constant</span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>σSB<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> sigmaSB <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">    alphaFS <span class="pl-k">=</span> <span class="pl-c1">7.2973525698e-3</span>  <span class="pl-c"><span class="pl-c">#</span>fine-structure constant</span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">globals</span>()[<span class="pl-s"><span class="pl-pds">&#39;</span>αFS<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> alphaFS  <span class="pl-c"><span class="pl-c">#</span> shorter alias (only works in Python 3)</span></td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>Constants--chemistry, atomic physics, electrons</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> Rgas, e, uBohr, uNuc, aBohr, me, mp, mn, Rinf, Ry, Hartree, \</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">           ARichardson, Phi0, KJos, RKlitz</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">    Rgas <span class="pl-k">=</span> kB <span class="pl-c"><span class="pl-c">#</span>ideal gas constant (see README)</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">    e <span class="pl-k">=</span> <span class="pl-c1">1.602176565e-19</span> <span class="pl-k">*</span> C  <span class="pl-c"><span class="pl-c">#</span>charge of proton</span></td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">    uBohr <span class="pl-k">=</span> <span class="pl-c1">9.27400968e-24</span> <span class="pl-k">*</span> J<span class="pl-k">/</span>T  <span class="pl-c"><span class="pl-c">#</span>Bohr magneton</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">    uNuc <span class="pl-k">=</span> <span class="pl-c1">5.05078353e-27</span> <span class="pl-k">*</span> J<span class="pl-k">/</span>T <span class="pl-c"><span class="pl-c">#</span>nuclear magneton</span></td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">    aBohr <span class="pl-k">=</span> <span class="pl-c1">0.52917721092e-10</span> <span class="pl-k">*</span> m  <span class="pl-c"><span class="pl-c">#</span>Bohr radius</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">    me <span class="pl-k">=</span> <span class="pl-c1">9.10938291e-31</span> <span class="pl-k">*</span> kg  <span class="pl-c"><span class="pl-c">#</span>electron mass</span></td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">    mp <span class="pl-k">=</span> <span class="pl-c1">1.672621777e-27</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span>proton mass</span></td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">    mn <span class="pl-k">=</span> <span class="pl-c1">1.674927351e-27</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span>neutron mass</span></td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">    Rinf <span class="pl-k">=</span> <span class="pl-c1">10973731.568539</span> <span class="pl-k">/</span> m <span class="pl-c"><span class="pl-c">#</span>Rydberg constant</span></td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">    Ry <span class="pl-k">=</span> <span class="pl-c1">2.179872171e-18</span> <span class="pl-k">*</span> J  <span class="pl-c"><span class="pl-c">#</span>Rydberg energy, approximately 13.6 eV</span></td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">    Hartree <span class="pl-k">=</span> <span class="pl-c1">2</span><span class="pl-k">*</span>Ry <span class="pl-c"><span class="pl-c">#</span>Hartree energy, approximately 27.2 eV</span></td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">    ARichardson <span class="pl-k">=</span> (<span class="pl-c1">4</span>.<span class="pl-k">*</span>pi<span class="pl-k">*</span>e<span class="pl-k">*</span>me<span class="pl-k">*</span>kB<span class="pl-k">**</span><span class="pl-c1">2</span>) <span class="pl-k">/</span> hPlanck<span class="pl-k">**</span><span class="pl-c1">3</span>  <span class="pl-c"><span class="pl-c">#</span>Richardson constant</span></td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">    Phi0 <span class="pl-k">=</span> <span class="pl-c1">2.067833758e-15</span> <span class="pl-k">*</span> Wb <span class="pl-c"><span class="pl-c">#</span>magnetic flux quantum</span></td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">    KJos <span class="pl-k">=</span> <span class="pl-c1">4.83597870e14</span> <span class="pl-k">*</span> Hz <span class="pl-k">/</span> V <span class="pl-c"><span class="pl-c">#</span>Josephson constant</span></td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">    RKlitz <span class="pl-k">=</span> <span class="pl-c1">2.58128074434e4</span> <span class="pl-k">*</span> ohm <span class="pl-c"><span class="pl-c">#</span>von Klitzing constant</span></td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>Constants--astronomical and properties of earth</span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">global</span> REarth, g0, Msolar, MEarth</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">    REarth <span class="pl-k">=</span> <span class="pl-c1">6371</span>. <span class="pl-k">*</span> km <span class="pl-c"><span class="pl-c">#</span>radius of earth</span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">    g0 <span class="pl-k">=</span> <span class="pl-c1">9.80665</span> <span class="pl-k">*</span> m <span class="pl-k">/</span> s<span class="pl-k">**</span><span class="pl-c1">2</span> <span class="pl-c"><span class="pl-c">#</span>standard earth gravitational acceleration</span></td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">    Msolar <span class="pl-k">=</span> <span class="pl-c1">1.98892e30</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span>mass of the sun</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">    MEarth <span class="pl-k">=</span> <span class="pl-c1">5.9736e24</span> <span class="pl-k">*</span> kg <span class="pl-c"><span class="pl-c">#</span>mass of earth</span></td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Set units randomly when this module is initialized. (Don&#39;t worry: If the</span></td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> module is imported many times from many places, this command will only</span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> execute during the first import.)</span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">reset_units()</td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><clipboard-copy class="dropdown-item" id="js-copy-lines" style="cursor:pointer;" data-original-text="Copy lines">Copy lines</clipboard-copy></li>
        <li><clipboard-copy class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</clipboard-copy></li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" href="/sbyrnes321/numericalunits/blame/ab608390f07102857b66ebb82e47ea426b5aec77/numericalunits.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" href="/sbyrnes321/numericalunits/issues/new">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form" action="" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" />
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.39091s from unicorn-2807931513-p0kjm">GitHub</span>, Inc.</li>
        <li class="mr-3"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://help.github.com/articles/github-security/" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>
    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://blog.github.com" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>

    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" integrity="sha512-2GVr5rsbbfKbHM6oRrri41+qJ2ltJBCqluASS29fj+9yHGLFmFhq0C64VMdL57UJ34G2+FXU+8FZhaAOnsCEhw==" type="application/javascript" src="https://assets-cdn.github.com/assets/compat-bb7abfb15ed4ffb0da9056d4c980fba5.js"></script>
    <script crossorigin="anonymous" integrity="sha512-ND8dytMkRT9WSjKCydnxt+zqWuc5E++ua212AKbBJxST19WRVBiHadyaMLJrVx71GsJsVgdmMupnpYSQ5tveoQ==" type="application/javascript" src="https://assets-cdn.github.com/assets/frameworks-8e1df5ef753f74d23d26e500300805ce.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-RscBUnX1a4pEf/Bj+kRymgUGA00g16HsFPhnX+lVqnqwMbCnKD7L1+o8Y4yaGUbrZnBOa3Or/OFgkqNN9v09BQ==" type="application/javascript" src="https://assets-cdn.github.com/assets/github-55f81da8b1061135c9e00bf129f6a0a4.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>

<div id="hovercard-aria-description" class="sr-only">
  Press h to open a hovercard with more details.
</div>


  </body>
</html>

