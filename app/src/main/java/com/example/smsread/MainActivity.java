package com.example.smsread;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import java.util.Arrays;

public class MainActivity extends AppCompatActivity {

    private TextView myTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        myTextView = findViewById(R.id.textView);
        ActivityCompat.requestPermissions(MainActivity.this,
                new String[]{Manifest.permission.READ_SMS}, PackageManager.PERMISSION_GRANTED);
    }

    public void Read_SMS(View view) {

        Cursor cursor = getContentResolver().query(Uri.parse("content://sms"), null,
                null, null, null);
        cursor.moveToFirst();

        myTextView.setText(cursor.getString(12));
        cursor.close();
        //passwordArray();
    }
//
//    public void passwordArray() {
//        String[] passwords = new String[10];
//        String sms = "@+id/textView";
//        int start = 15;
//        int end = start + 7;
//        for(int i = 0; i < passwords.length; i++) {
//            passwords[i] = sms.substring(start, end);
//            start = end + 1;
//            end = start + 7;
//
//        }

    }


