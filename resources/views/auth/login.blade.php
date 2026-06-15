<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="theme-color" content="#5955D1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Log In | CMS Admin Panel</title>
  
  <link rel="icon" type="image/png" href="/assets/images/favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/assets/libs/flaticon/css/all/all.css">
  <link rel="stylesheet" href="/assets/libs/lucide/lucide.css">
  <link rel="stylesheet" href="/assets/libs/fontawesome/css/all.min.css">
  <link rel="stylesheet" href="/assets/libs/simplebar/simplebar.css">
  <link rel="stylesheet" href="/assets/libs/node-waves/waves.css">
  
  <link rel="stylesheet" href="/assets/css/styles.css">

  <style>
    body {
        background-color: #f1f1f1;
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    .login-box {
        width: 100%;
        max-width: 400px;
        padding: 20px;
    }
    .login-logo {
        text-align: center;
        margin-bottom: 20px;
        font-size: 24px;
        font-weight: bold;
    }
    .login-card {
        background: #fff;
        padding: 24px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.13);
    }
    .form-control {
        border-radius: 4px;
    }
    .btn-primary {
        width: 100%;
        border-radius: 4px;
    }
  </style>
</head>
<body>
  <div class="login-box">
    <div class="login-logo">
      Laravel CMS
    </div>
    <div class="login-card">
      <form action="{{ route('login') }}" method="post">
        @csrf
        <div class="mb-3">
          <label for="email" class="form-label">Email Address</label>
          <input type="email" class="form-control @error('email') is-invalid @enderror" id="email" name="email" value="{{ old('email') }}" required autofocus>
          @error('email')
            <div class="invalid-feedback">{{ $message }}</div>
          @enderror
        </div>
        <div class="mb-4">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control" id="password" name="password" required>
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="remember" name="remember">
          <label class="form-check-label" for="remember">Remember Me</label>
        </div>
        <button type="submit" class="btn btn-primary">Log In</button>
      </form>
      <div class="mt-3 text-center">
        <a href="{{ route('register') }}" class="text-decoration-none">Don't have an account? Register</a>
      </div>
    </div>
  </div>
</body>
</html>
