package com.example.nerdherd;

import android.content.Context;
import android.content.Intent;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class LoginActivity extends AppCompatActivity {

    Button login;
    EditText login_password;
    EditText login_email;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        //initializing components
        login = findViewById(R.id.login);
        login_password = findViewById(R.id.login_password_field);
        login_email = findViewById(R.id.login_email_field);

        //setting onclick listeners for buttons
        login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = LoginActivity.this;

                if (accountVerification()) {
                    //login is successful so then move to the main page
                    Class mainPageActivity = MainPageActivity.class;
                    Intent intent = new Intent(context, mainPageActivity);
                    startActivity(intent);
                } else {
                    //Display to the user incorrect login entered message
                    AlertDialog.Builder incorrectLoginAlert =  new AlertDialog.Builder(context);
                    incorrectLoginAlert.setMessage("Incorrect Email/Password");
                    incorrectLoginAlert.setPositiveButton("OK", null);
                    incorrectLoginAlert.setCancelable(true);
                    incorrectLoginAlert.create().show();
                }
            }
        });
    }


    public boolean accountVerification(){
        //TODO check if email and password are a correct match
        String email = login_email.getText().toString();
        String password = login_password.getText().toString();
        return false;
    }
}
