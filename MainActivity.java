// MainActivity.java
package com.example.yourapp;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        WebView myWebView = new WebView(this);
        setContentView(myWebView);

        WebSettings webSettings = myWebView.getSettings();
        webSettings.setJavaScriptEnabled(true); // React chalane ke liye zaroori hai

        // Replit ka LIVE URL yahan dalein
        myWebView.loadUrl("https://aapka-project-naam.replit.app"); 

        myWebView.setWebViewClient(new WebViewClient());
    }
}